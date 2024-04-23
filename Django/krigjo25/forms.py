from tkinter import Widget
from unittest.util import _MAX_LENGTH


from django import forms

class CommentForm(forms.Form):

    author = forms.CharField(
        max_length=60, 
        widget = forms.TextInput(attrs= { "class": "form-control", "placeholder": 'Name'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Leave a comment'}))