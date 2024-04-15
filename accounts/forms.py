from django import forms
from .models import UserAuthDataModels, ProfileModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class SavePasswordForm(forms.ModelForm):
    class Meta:
        model = UserAuthDataModels
        fields = ['username', 'password']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['img', 'age', 'bio']
