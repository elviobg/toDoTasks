from django.forms import ModelForm
from .models import Category, Task

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    fields = '__all__'

class TaskForm(ModelForm):
  class Meta:
    model = Task    
    fields = '__all__'