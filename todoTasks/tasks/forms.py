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

  def __init__(self, user=None, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)    
    if user is not None:
      self.fields['category'].queryset = Category.objects.filter(user=user)