from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['name','email','phone','password']

class UserLoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)


  