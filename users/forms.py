from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')
        error_messages = {
            'username': {'unique': "User with this username already exists."},
            'email': {'unique': 'User with this email already exists.'}
        }


