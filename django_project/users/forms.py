# We will crete a form that inherits from the inbuilt user creation form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # This class Meta give us a nested namespace for configurations and keeps the configurations in one place
    # The model that is going to be affected iss the User model
    # The fields that we have in the list are the fields that we want in the specified order

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Here we create a model form. A model form allows us to update a specific database model.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

