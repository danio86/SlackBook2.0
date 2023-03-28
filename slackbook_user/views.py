from django.shortcuts import render, redirect
from .models import User


def home(request):

    context = {

    }
    return render(request, 'base/index.html', context)
