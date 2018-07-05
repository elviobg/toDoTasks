from django.urls import path
from .views import new_category, new_task, list_categories

app_name = 'tasks'

urlpatterns = [
  #Create
  path('category/insert', new_category, name='url_category_insert'),
  path('task/insert', new_task, name='url_task_insert'),
  #read
  path('category', list_categories, name='url_category'),
  #update
  #delete
]