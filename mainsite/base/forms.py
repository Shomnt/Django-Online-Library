from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(help_text="Correct email, please", required=True)
    class Meta:
        model = User
        exclude = ('first_name', 'last_name')
        fields = ('id_user', 'username', 'email')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ('first_name', 'last_name')
        fields = ('id_user', 'username', 'email', 'password')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())