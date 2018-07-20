from django.urls import path
from .views import create_category, create_task, list_categories, update_task, delete_task, update_category, delete_category
app_name = 'tasks'

urlpatterns = [
  #Create
  path('category/insert', create_category, name='url_category_insert'),
  path('task/insert', create_task, name='url_task_insert'),
  #read
  path('category', list_categories, name='url_category'),
  #update  
  path('task/update/<int:pk>', update_task, name='url_task_update'),
  path('category/update/<int:pk>', update_category, name='url_category_update'),  
  #delete
  path('task/delete/<int:pk>', delete_task, name='url_task_delete'),
  path('category/delete/<int:pk>', delete_category, name='url_category_delete'),
]