from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import Users


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Users
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'avatar')
