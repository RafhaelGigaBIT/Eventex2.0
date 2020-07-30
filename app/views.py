from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import *

# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    user = request.user
    tags = Tag.objects.filter(user=user)
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

def addEvent(request, pk):
    tag = Tag.objects.get(id=pk)
    if tag.user == request.user:
        form = EventForm()
        event = Event.objects.all()
        context = {'events':event, 'form': form, 'tag':tag}

        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.tag = tag
                post.save()
                messages.success(request, 'Evento adcionado com sucesso!!')
                return redirect('/add-event/{}'.format(tag.id))
            else:
                print('Deu errade aeee')

        return render(request, 'app/add-event.html', context)
    else:
        return redirect('/')


def actEvent(request, pk):
    pass