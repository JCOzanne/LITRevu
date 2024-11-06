from django import forms
from django.contrib.auth import get_user_model
from . import models

CustomUser=get_user_model()


class BlogForm(forms.ModelForm):
    edit_blog=forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model=models.Blog
        fields=['title', 'content','image']
        labels = {
            'title': 'Titre',
            'content': 'Contenu',
            'image' : 'Image'
        }

class DeleteBlogForm(forms.Form):
    delete_blog=forms.BooleanField(widget=forms.HiddenInput, initial=True)

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['follows']