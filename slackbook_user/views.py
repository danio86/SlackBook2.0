from django.shortcuts import render, redirect
from .models import User, Channel, Topic, Post
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from .forms import ChannelForm, UserForm
from .forms import ChannelForm, UserForm


def home(request):
    s = request.GET.get('s') if request.GET.get('s') is not None else ''

    queryset = Channel.objects.filter(
        Q(topic__title__icontains=s) |
        Q(title__icontains=s) |
        Q(content__icontains=s)
    )

    topics = Topic.objects.all()[0:6]
    channels = Channel.objects.all()

    context = {
        'topics': topics, 'channels': channels, 'queryset': queryset
    }
    return render(request, 'base/index.html', context)


def channel(request, pk):
    queryset = Channel.objects.get(id=pk)
    posts = queryset.post_set.all().order_by('-created_on')
    # this gives all attributes of the Channel-Model-Child Post
    guests = queryset.guests.all()

    if request.method == 'POST':
        post = Post.objects.create(
            user=request.user,
            channel=queryset,
            body=request.POST.get('body'),
        )
        # .create is a django function

        queryset.guests.add(request.user)
        # this makes everybody a guest of the channel who posts something
        return redirect('channel', pk)

    context = {'channel': queryset, 'posts': posts, 'guests': guests}
    return render(request, 'base/channel.html', context)


def channelMember(request, pk):
    queryset = Channel.objects.get(id=pk)
    # queryset = Channel.objects.all()
    guests = queryset.guests.all()

    context = {'guests': guests}
    return render(request, 'base/channel-member.html', context)

# def topics(request):
#     queryset = Topic.objects.all()
#     context = {'channel': queryset}
#     return render(request, 'base/topics.html', context)


def account(request, pk):
    queryset = User.objects.get(id=pk)
    user_channels = queryset.channel_set.all()
    # this gives the whole Channel Model of the User with the right id
    # channels in context need to be called channels
    # because channel_availiable.html asks for channels!il
    user_comments = queryset.post_set.all()
    categories = Topic.objects.all()

    # channel_count = Channel.objects.count()
    channel_count = user_channels.count()

    context = {'user': queryset, 'channels': user_channels,
               'comments': user_comments, 'topics': categories,
               'channel_count': channel_count}
    return render(request, 'base/account.html', context)


@login_required(login_url='/accounts/login/')
def userSettings(request):
    user = request.user
    user_form = UserForm(instance=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)

        user_form.username = request.POST.get('username')
        user_form.email = request.POST.get('email')
        if user_form.is_valid():
            user_form.save()
        else:
            messages.error(request, 'Please only enter letters.')
            return redirect('/user-settings/')

        return redirect('user-account', user.id)

    context = {'user_form': user_form}
    return render(request, 'base/user-settings.html', context)


@login_required(login_url='/accounts/login/')
def deleteComment(request, pk):
    object = Post.objects.get(id=pk)
    channelId = object.channel.id

    context = {'object': object}
    if request.method == 'POST':
        object.delete()
        return redirect('channel', channelId)

    return render(request, 'base/delete.html', context)


@login_required(login_url='/accounts/login/')
def createChannel(request):
    form = ChannelForm()
    categories = Topic.objects.all()

    if request.method == 'POST':
        # method of the form in channel_form.html
        form = ChannelForm(request.POST)
        # this passis the POST into the form automatically.
        category_title = request.POST.get('topic')
        category, created = Topic.objects.get_or_create(title=category_title)
        # get_or_create() is a method which gets or creates an object

        instance = Channel.objects.create(
            host=request.user,
            topic=category,
            title=request.POST.get('topic-name'),
            description=request.POST.get('description'),
            # title from the frontend
            private=request.POST.get('private'),
            # guests=request.POST.get('guests'),
            )
        # instance.guests.add(request.POST.get('guests'))

        return redirect('home')
    context = {'form': form, 'categories': categories}
    return render(request, 'base/create-channel.html', context)


@login_required(login_url='/accounts/login/')
def updateChannel(request, pk):
    queryset = Channel.objects.get(id=pk)
    form = ChannelForm(instance=queryset)
    categories = Topic.objects.all()
    # this shows the prefild form to edit (instance is important!)
    groups_member = queryset.guests.all()

    # if request.user != queryset.host:
    #     return HttpResponse('You are not authorized!')

    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=queryset)
        # this only updates the form. It doesn't refill it.

        category_name = request.POST.get('topic')
        category, created = Topic.objects.get_or_create(title=category_name)

        queryset.title = request.POST.get('topic-name')
        queryset.topic = category
        queryset.description = request.POST.get('description')
        queryset.private = request.POST.get('private')
        # queryset.guests = groups_member.update('guests')
        print(queryset.private)
        if queryset.private == 'True':
            queryset.guests.add(request.POST.get('guests'))
        else:
            pass

        queryset.save()

        return redirect('home')

    context = {'form': form, 'categories': categories, 'queryset': queryset}
    return render(request, 'base/create-channel.html', context)


@login_required(login_url='/accounts/login/')
def deleteChannel(request, pk):
    object = Channel.objects.get(id=pk)

    # if request.user != object.host:
    #     return HttpResponse('You are not authorized!')

    context = {'object': object}
    if request.method == 'POST':
        object.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)
