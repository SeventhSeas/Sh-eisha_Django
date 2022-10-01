
from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *
from django.forms import ModelForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content']
       


class Meta:
		model = Comment
		fields = ('post', 'autor', 'text',)   


        