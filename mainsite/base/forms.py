from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

from django.forms.widgets import PasswordInput, TextInput

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ('first_name', 'last_name')
        fields = ('id_user', 'username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ('first_name', 'last_name')
        fields = ('id_user', 'username', 'email', 'password')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())