from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
  class Meta:
    model = User
    #fields = (''__all__'')
    fields = ('first_name', 'last_name', 'username', 'password')