from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import Users


class ProfileForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'avatar',)

    first_name = forms.CharField()
    last_name = forms.CharField()
    avatar = forms.ImageField(required=False)
