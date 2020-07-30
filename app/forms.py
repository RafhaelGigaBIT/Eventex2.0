from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'place', 'invitations', 'description', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'autocomplete': 'off','class': ' form-control form-control form-control-alternative','placeholder': 'Event Title', 'id': 'event-title'}),
            'place': forms.TextInput(attrs={'autocomplete': 'off','class': ' form-control form-control form-control-alternative','placeholder': 'Event Place'}),
            'invitations': forms.NumberInput(attrs={'autocomplete': 'off','class': ' form-control form-control form-control-alternative','placeholder': 'Event Invites'}),
            'description': forms.Textarea(attrs={'style':'height:80px','autocomplete': 'off','class': ' form-control form-control form-control-alternative','placeholder': 'Event Description'}),
            'date': forms.DateInput(attrs={'type':'date','id':'datePicker'})
        }