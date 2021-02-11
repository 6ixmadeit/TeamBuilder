from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Fixture


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
    	model  = User
    	fields = ("email", "first_name", "last_name","password1", "password2", "user_type", "team")

class FixtureForm(forms.Form):
    class Meta:
    	model  = Fixture
    	fields = ("team1", "team2", "address_1", "address_2", "city", "zip_code", "date")