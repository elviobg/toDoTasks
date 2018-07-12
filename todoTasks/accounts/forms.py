from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):  
  password = forms.CharField(widget=forms.PasswordInput(), label="Senha")  
  class Meta:
    model = User    
    fields = ('first_name', 'last_name', 'username', 'password')
    labels = {
      'first_name': 'Nome', 
      'last_name': 'Sobrenome', 
      'username': 'Login'
      }