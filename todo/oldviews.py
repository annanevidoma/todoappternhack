from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import NewTask

class TaskForm(forms.Form):
    task = forms.CharField()
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            task = form.cleaned_data['task']
            print(task)
            # ...
            # redirect to a new URL:
            return HttpResponse('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'index.html', {'form': form})
# Create your views here.

def index(request):
    return render(request, "todo/index.html")  

#2
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
       task = forms.CharField(label="New Task")

tasks = []
def index2 (request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todo/index.html", {
        "tasks":request.session["tasks"]
         })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse( "tasks:index"))
        else:
            return render(request,"todo/index.html", {
                "form":form
            })
        

    return render(request, "todo/index.html",{
        "form":NewTaskForm(),
    })

#3
def index3 (request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
   
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse( "todo:index"))
        else:
            return render(request,"todo/index.html", {
                "form":form
            })
    return render(request, "todo/index.html", {
        "tasks":request.session["tasks"],
        "form":NewTaskForm(),
         })

#4
def index4 (request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
   
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse( "todo:index"))
        else:
            return render(request, "todo/index.html", {
                "form":form
            })
    return render(request, "todo/index.html", {
        "tasks":request.session["tasks"],
        "form":NewTaskForm(),
       })
#5
def index5 (request):
    allTasks = NewTask.objects.all()
    if "tasks" not in request.session:
        request.session["tasks"] = []
   
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse( "todo:index"))
        else:
            return render(request, "todo/index.html", {
                "form":form
            })
    
    return render(request, "todo/index.html", {
        "tasks":request.session["tasks"],
        "form":NewTaskForm(),
        "allTasks":allTasks,
    })
