from django.urls import path
from .views import create_category, create_task, list_categories, delete_task

app_name = 'tasks'

urlpatterns = [
  #Create
  path('category/insert', create_category, name='url_category_insert'),
  path('task/insert', create_task, name='url_task_insert'),
  #read
  path('category', list_categories, name='url_category'),
  #update
  #path('category', update_task, name='url_category_update'),
  #delete
  path('task/delete/<int:pk>', delete_task, name='url_category_delete'),  
]