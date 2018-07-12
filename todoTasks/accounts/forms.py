from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):    
  class Meta:
    model = User    
    fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
    labels = {
      'first_name': 'Nome', 
      'last_name': 'Sobrenome', 
      'username': 'Login',
      'password1': 'Senha',
      'password2': 'Confirmação da senha',
      }