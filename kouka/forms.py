from django import forms
from .models import Comment, PhotoPost

class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','topic']
