from django.shortcuts import render, redirect
from .models import User, Channel, Topic, Post


def home(request):
    r = request.GET.get('r') if request.GET.get('r') is not None else ''
    queryset = Topic.objects.all()[0:6]
    channels = Channel.objects.all()

    context = {
        'topics': queryset, 'channels': channels
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


def topics(request):
    queryset = Topic.objects.all()
    context = {'channel': queryset}
    return render(request, 'base/topics.html', context)


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
