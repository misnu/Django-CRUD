from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':"Enter Task"
    }))
    class Meta:
        model = Task
        fields = '__all__'