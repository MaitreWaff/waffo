from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from profiles.models import Profile

# CONSTANTES
FN_MAX_L    = 30
LN_MAX_L    = 30
LOC_MAX_L   = 50
EMAIL_MAX_L = 254

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields  = ('url', 'location', 'company')

class SignUpForm(UserCreationForm):
    first_name  = forms.CharField(max_length=FN_MAX_L, required=False, help_text='Optional.')
    last_name   = forms.CharField(max_length=LN_MAX_L, required=False, help_text='Optional.')
    email       = forms.EmailField(max_length=EMAIL_MAX_L, help_text='Required. Inform a valid email address.')

    # Profile
    bio         = forms.TextInput()
    location    = forms.CharField(max_length=LOC_MAX_L, required=False, help_text='Ville Actuelle.')
    date_naiss  = forms.DateField()

    class Meta:
        model   = Profile
        fields  = ('username', 'first_name', 'last_name', 'email', 'location', 'date_naiss', 'password1', 'password2', 'bio')















