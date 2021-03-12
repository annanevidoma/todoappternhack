from django import forms
from django.db import models
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewTaskForm
from .models import NewTask
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


tasks = []
@login_required
def index (request):
    tasks = NewTask.objects.all()

    form = NewTaskForm()

    if request.method =='POST':
	    form = NewTaskForm(request.POST)
	    if form.is_valid():
		    form.save()
	    return redirect('/')


    context = {'tasks':tasks, 'form':form}
    return render(request, 'todo/index.html', context)



def sign_up(request):
   
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('')
    context['form']=form
    return render(request,'todo/sign-up.html', context)

def sign_in(request):
    if request.user.is_authenticated:
	    return redirect('/')
    else:
	    if request.method == 'POST':
		    username = request.POST.get('username')
		    password =request.POST.get('password')
		    user = authenticate(request, username=username, password=password)

		    if user is not None:
			    login(request, user)
			    return redirect('/')
		    else:
			    messages.info(request, 'Username OR password is incorrect')

	    context = {}
	    return render(request, 'todo/sign-in.html', context)

def completed(request, todo_id):
   
    item = NewTask.objects.get(id=todo_id)

    if request.method == 'POST':
	    item.delete()
	    return redirect('/')

    context = {'item':item}
    return render(request, 'todo/index.html', context)

