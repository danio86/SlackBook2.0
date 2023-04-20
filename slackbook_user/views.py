from django.shortcuts import render, redirect
from .models import User, Channel, Topic, Post, Chat
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from .forms import ChannelForm, UserForm
from .forms import ChannelForm, UserForm, PostForm, ChatForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    s = request.GET.get('s') if request.GET.get('s') is not None else ''

    queryset = Channel.objects.filter(
        Q(topic__title__icontains=s) |
        Q(title__icontains=s) |
        Q(content__icontains=s)
    )

    topics = Topic.objects.all()[0:6]
    channels = Channel.objects.all()
    users = User.objects.all().order_by('-loggedin')
    # guests = users.guests.all()

    comments = Post.objects.all().order_by('-created_on').filter(
        Q(channel__topic__title__icontains=s))[0:3]
    # Q(channel__title__icontains=s))
    # this filters by the title of the topic of the channel
    # if the url ending is in channel title

    context = {
        'topics': topics, 'channels': channels, 'queryset': queryset,
        'comments': comments, 'users': users, 
    }
    return render(request, 'base/index.html', context)


def channel(request, pk):
    queryset = Channel.objects.get(id=pk)
    posts = queryset.post_set.all().order_by('-created_on')
    # this gives all attributes of the Channel-Model-Child Post
    guests = queryset.guests.all()
    post_form = PostForm()

    if request.method == 'POST':
        # post_form = PostForm(request.FILES)
        posts = Post.objects.create(
                user=request.user,
                channel=queryset,

            )
        post_form = PostForm(request.POST, request.FILES, instance=posts)
        # post_form = PostForm(request.POST, request.FILES)

        post_form.body = request.POST.get('body')
        post_form.image = request.POST.get('image')
    #     post_form.image_description = request.POST.get('image_description')
        if post_form.is_valid():
            post_form.save()
            # posts = Post.objects.create(
            #     user=request.user,
            #     channel=queryset,
            #     body=post_form.body,
            #     image=post_form.image,
            # )
            queryset.guests.add(request.user)
            return redirect('channel', pk)
        # else:
        #     messages.error(request, 'Please only enter letters.')
        #     return redirect('channel', pk)

    # if request.method == 'POST':
    #     post = Post.objects.create(
    #         user=request.user,
    #         channel=queryset,
    #         body=request.POST.get('body'),
    #         image=request.POST.get('image'),
    #     )
        # .create is a django function

        # queryset.guests.add(request.user)
        # this makes everybody a guest of the channel who posts something
        return redirect('channel', pk)

    context = {'channel': queryset, 'posts': posts, 'guests': guests,
               'post_form': post_form}
    return render(request, 'base/channel.html', context)


def chat(request, pk):
    queryset = Chat.objects.get(id=pk)
    posts = queryset.post_set.all().order_by('-created_on')
    
    post_form = PostForm()

    if request.method == 'POST':
        posts = Post.objects.create(
                user=request.user,
                chat=queryset,

            )
        post_form = PostForm(request.POST, request.FILES, instance=posts)

        post_form.body = request.POST.get('body')
        post_form.image = request.POST.get('image')

        if post_form.is_valid():
            post_form.save()

            return redirect('chat', pk)

    context = {'chat': queryset, 'posts': posts,
               'post_form': post_form}
    return render(request, 'base/chat.html', context)


def channelMember(request, pk):
    queryset = Channel.objects.get(id=pk)
    # queryset = Channel.objects.all()
    guests = queryset.guests.all()

    context = {'guests': guests}
    return render(request, 'base/channel-member.html', context)


def account(request, pk):
    queryset = User.objects.get(id=pk)
    # chat = Chat.objects.get(id=request.user.id)
    chat = Chat.objects.all()
    user_channels = queryset.channel_set.all()
    all_Channels = Channel.objects.all()
    guests = queryset.guests.all()
    user_comments = queryset.post_set.all()
    categories = Topic.objects.all()

    # posts = queryset.post_set.all().order_by('-created_on')
    # post_form = PostForm()

    # if request.method == 'POST':
    #     posts = Post.objects.create(
    #             user=queryset,
    #             chat=chat,

    #         )
    #     post_form = PostForm(request.POST, request.FILES, instance=posts)

    #     post_form.body = request.POST.get('body')
    #     post_form.image = request.POST.get('image')
    #     if post_form.is_valid():
    #         post_form.save()

            # return redirect('chat', pk)

    # channel_count = Channel.objects.count()
    channel_count = user_channels.count()
    joined_count = guests.count() - channel_count
    # for chan in Channel.objects.all():
    #     if queryset.username == chan.guests:
    #         joinded_count += 1

    # posts = queryset.post_set.all().order_by('-created_on')
    # post_form = PostForm()

    # if request.method == 'POST':
    #     posts = Post.objects.create(
    #             user=queryset,
    #             chat=chat,

    #         )
    #     post_form = PostForm(request.POST, request.FILES, instance=posts)

    #     post_form.body = request.POST.get('body')
    #     post_form.image = request.POST.get('image')
    #     if post_form.is_valid():
    #         post_form.save()

            # return redirect('chat', pk)

    form = ChatForm()

    if request.method == 'POST':
        form = ChatForm(request.POST)

        Chat.objects.create(
            host=queryset,
            title=request.user.username,
            body=request.POST.get('body'),
            # title from the frontend
            )
        if form.is_valid():
            form.save()
            # return redirect('chat', form.id)
        
        return redirect('chat', chat[0].id)
        # return redirect('home')

    context = {'user': queryset, 'channels': user_channels,
               'comments': user_comments, 'topics': categories,
               'channel_count': channel_count, 'joined_count': joined_count,
               'form': form, 'categories': categories, 'chat': chat,
               'all_Channels': all_Channels, 'guests': guests}
    return render(request, 'base/account.html', context)


def topics(request):
    s = request.GET.get('s') if request.GET.get('s') is not None else ''

    queryset = Channel.objects.filter(
        Q(topic__title__icontains=s) |
        Q(title__icontains=s) |
        Q(content__icontains=s)
    )

    topics = Topic.objects.all()

    context = {'topics': topics, 'queryset': queryset, }
    return render(request, 'base/topics.html', context)


@login_required(login_url='/accounts/login/')
def userSettings(request):
    user = request.user
    user_form = UserForm(instance=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)

        user_form.username = request.POST.get('username')
        user_form.email = request.POST.get('email')
        if user_form.is_valid():
            user_form.save()
        else:
            messages.error(request, 'Please only enter letters.')
            return redirect('/user-settings/')

        return redirect('home')
        # return redirect('user-settings')
        # return redirect('user-account', user.id)

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
def createPersonalChannel(request):

    form = ChatForm()
    # categories = Topic.objects.all()

    if request.method == 'POST':
        form = ChatForm(request.POST)
        # category_title = 'test1'
        # category, created = Topic.objects.get_or_create(title=category_title)
        # get_or_create() is a method which gets or creates an object

        Chat.objects.create(
            host=request.user,
            title='test4',
            body=request.POST.get('body'),
            # title from the frontend
            )
        if form.is_valid():
            form.save()
        # instance.guests.add(request.POST.get('guests'))

        return redirect('home')
    context = {'form': form}
    # context = {'form': form, 'categories': categories}
    return render(request, 'base/create-personal-channel.html', context)


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


@login_required(login_url='/accounts/login/')
def logoutUser(request):
    request.user.loogedin = False
    logout(request)
    return redirect('home')


# def logout(request):
#     user = request.user
#     user_form = UserForm(instance=user)

#     if request.method == 'POST':

#         user_form.loggedin = request.POST.get('loggedin')
#         if user_form.is_valid():
#             user_form.save()
#         else:
#             messages.error(request, 'Please only enter letters.')
#             return redirect('/logout/')

#         return redirect('logout')

#     context = {}
#     return render(request, 'base/account/logout.html', context)
