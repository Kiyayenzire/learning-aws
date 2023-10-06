# uer registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# user login
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from . models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2' }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


#profile management update
class UpdateUserForm(forms.ModelForm):
    password = None # dont want to update password, update only username and email
    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']
    

# updating profile pcture
class UpdateProfilePicForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['profile_pic']
