from django.urls import path
from .views import new_category, new_task

app_name = 'tasks'

urlpatterns = [
  path('category/insert', new_category, name='url_category_insert'),
  path('task/insert', new_task, name='url_task_insert'),
]