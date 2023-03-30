from django.shortcuts import render, redirect
from .models import User, Channel, Topic


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

    context = {
        'channel': queryset
    }
    return render(request, 'base/channel.html', context)


def topics(request):
    queryset = Topic.objects.all()
    context = {'channel': queryset}
    return render(request, 'base/topics.html', context)
