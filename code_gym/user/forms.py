from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': "max-width:300px",
                'placeholder': "username"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'password1': PasswordInput(attrs={
                'class': "form-control",
                'style': "max-width:300px",
                'placeholder': "password"
            }),
            'password2': PasswordInput(attrs={
                'class': "form-control",
                'style': "max-width:300px",
                'placeholder': "password"
            }),
        }


class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
