from django.forms import ModelForm
from .models import Category, Task

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    exclude = ('user',)

class TaskForm(ModelForm):
  class Meta:
    model = Task    
    exclude = ('user',)