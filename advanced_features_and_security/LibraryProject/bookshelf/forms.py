from django import forms
from .models import Book

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(label = "Email")