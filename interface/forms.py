from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=140)
    # email = forms.EmailField(max_length=140)
    password = forms.CharField(max_length=140, widget=forms.PasswordInput)
