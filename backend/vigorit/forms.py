from django import forms
from .models import AppUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class AppUserForm(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = ('name', 'age', 'height', 'weight', 'sex')
