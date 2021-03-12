from django import forms
from django.db import models
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import NewTask



class NewTaskForm(ModelForm):
    class Meta():
        model = NewTask
        fields = ['task']
        
