from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from profiles.models import *

# CONSTANTES
FN_MAX_L    = 30
LN_MAX_L    = 30
LOC_MAX_L   = 50
EMAIL_MAX_L = 254
UN_MAX_L    = 30
PWD_MAX_L   = 30


# Refaccto
class RegisterUserform(forms.ModelForm):
    """Formulaire de Creation de Profile Utilisateur."""
    password    = forms.CharField(widget=forms.PasswordInput)
    password2   = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model   = User

        fields  = ('username', 'email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']



class SignUpForm(UserCreationForm):
    """Formulaire de Creation de Profile Utilisateur."""

    # first_name  = forms.CharField(max_length=FN_MAX_L, required=False, help_text='Optionel.')
    # last_name   = forms.CharField(max_length=LN_MAX_L, required=False, help_text='Optionel.')

    # email       = forms.EmailField(max_length=EMAIL_MAX_L, help_text='Requis. Entrez une adresse email valide.')

    # Profile
    # bio         = forms.TextInput()
    # location    = forms.CharField(max_length=LOC_MAX_L, required=False, help_text='Ville Actuelle.')
    # date_naiss  = forms.DateField()

    class Meta:
        model   = User
        fields  = ('username', 'email', 'password', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = ('first_name', 'last_name', 'email')

class ProfileForm(UserCreationForm):
    class Meta:
        model = UserProfileModel
        exclude = ('photo',)
        # fields  = ('url', 'location', 'company')


class ViewProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        # exclude = ('photo',)
        fields  = ('mobile', 'sexe', 'bio', 'location', 'date_naiss')










class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=UN_MAX_L, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=PWD_MAX_L, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'username'}))

class SignInForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password',)

class UpdateProfileForm(UserCreationForm):
    # first_name  = forms.CharField(max_length=FN_MAX_L, required=False, help_text='Optionel.')
    # last_name   = forms.CharField(max_length=LN_MAX_L, required=False, help_text='Optionel.')
    email       = forms.EmailField(max_length=EMAIL_MAX_L, help_text='Requis. Entrez une adresse email valide.')

    # Profile
    # bio         = forms.TextInput()
    # location    = forms.CharField(max_length=LOC_MAX_L, required=False, help_text='Ville Actuelle.')
    # date_naiss  = forms.DateField()

    class Meta:
        model   = UserProfileModel
        fields  = ('user', 'email', 'password1', 'password2')
        # fields  = ('username', 'email', 'password1', 'password2')















