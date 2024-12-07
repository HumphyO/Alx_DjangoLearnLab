from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from taggit.forms import TagField, TagWidget

#Create user form
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self ,commit=True):
        user = super().save(commit=False)
        user.email = self.clean_data('email')
        if commit:
            user.save()
            return user

class PostForm(forms.ModelForm):
    tags = TagField(required=False, widget=TagWidget())
    
    class Meta:
        models = Post
        fields = ['title', 'content']
        widgets = {
            'tags': TagWidget
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        