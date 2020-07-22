from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    user = request.user
    tags = Tag.objects.all()
    events = Event.objects.filter(user=request.user)
    context = {'user':user, 'tags':tags, 'events':events, 'count':events.count()}
    return render(request, 'app/index.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)      
    user = request.user
    context = {'user':user, 'event':event}
    if event.user == request.user:
        return render(request, 'app/event.html', context)
    else:
        return redirect('/')

def actEvent(request, pk):
    event = Event.objects.get(id=pk) 
    if event.user == request.user:
        context = {'event':event}
        return render(request, 'app/activities.html', context)
    else:
        return redirect('/')