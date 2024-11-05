from django import forms
from . import models


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