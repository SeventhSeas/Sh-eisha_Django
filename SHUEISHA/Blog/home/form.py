
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from froala_editor.widgets import FroalaEditor
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }


class Meta:
		model = Comment
		fields = ('post', 'autor', 'text',)   


        