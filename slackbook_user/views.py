from django.shortcuts import render, redirect
from .models import User, Channel, Topic


def home(request):
    queryset = Channel.objects.all

    context = {
        'channels': queryset,
    }
    return render(request, 'base/index.html', context)


def channel(request, pk):
    queryset = Channel.objects.get(id=pk)

    context = {
        'channel': queryset
    }
    return render(request, 'base/channel.html', context)


def topics(request):
    queryset = Channel.objects.all()

    context = {'channel': queryset}
    return render(request, 'base/topics.html', context)
