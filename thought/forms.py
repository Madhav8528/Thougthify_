from django import forms
from .models import createthought
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ThoughtForm(forms.ModelForm):
    class Meta:
        model = createthought
        fields = ['text','image']


class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')