"""Module contains forms needed for registration page"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile


class RegistrationForm(UserCreationForm):
    """Class contains registration form using django UserCreationForm and related functions"""
    email = forms.EmailField()
    username = forms.CharField()
    private_policy = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['first_name'].widget.attrs.update({'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Password'})

    def clean_username(self):
        """Checks whether username exists in database"""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"The email {username} is already taken")
        return username

    def clean_email(self):
        """Checks whether email exists in database"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"The email {email} is already taken.")
        return email

    def save(self, commit=True):
        """Saves UserProfile object and User object"""
        user = User(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password1'])
        user_profile = UserProfile(
            user=user,
        )
        if commit:
            user.save()
            user_profile.save()
        return user
