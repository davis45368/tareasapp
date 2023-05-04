from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'importante']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-secondary-subtle', 'placeholder': 'Escribe un titulo' }),
            'description': forms.Textarea(attrs={'class': 'form-control bg-secondary-subtle', 'placeholder': 'Escribe una descripción'}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-1'})
        }