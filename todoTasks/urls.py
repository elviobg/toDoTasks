"""todoTasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''
from django.contrib import admin
from django.urls import path, include
from todoTasks.core.views import home
from todoTasks.tasks.views import new_category, new_task


urlpatterns = [
  path('', home, name='url_home'),  
  path('admin/', admin.site.urls),
  path('category/insert', new_category, name='url_category_insert'),
  path('task/insert', new_task, name='url_task_insert'),
]
'''
from django.contrib import admin
from django.urls import path, include
from todoTasks.core.views import home

urlpatterns = [
  path('', home, name='url_home'),  
  path('admin/', admin.site.urls),  
  path('', include('todoTasks.tasks.urls', namespace="tasks_app")),
]
