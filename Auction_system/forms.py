from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.images import get_image_dimensions
#from auction_system.models import UserProfile


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label='Email address', max_length=75)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user




