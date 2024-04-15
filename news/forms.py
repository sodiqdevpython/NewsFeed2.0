from django import forms
from .models import ContactModel, News, CommentModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'body']


class UpdateNews(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', 'image', 'type', 'status']

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', 'image', 'type', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text']