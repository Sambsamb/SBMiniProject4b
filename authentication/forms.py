"""
INF601 - Advanced Programming in Python
Mini Project 4 - Django small web app
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/6/2022
"""
# authentication/forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    # The PasswordInput widget automatically hides the input from view
    # by rendering an HTML <input> with type=”password”.


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

