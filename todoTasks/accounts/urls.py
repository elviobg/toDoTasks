from django.urls import path
from .views import add_user, user_login

app_name = 'accounts'

urlpatterns = [
  path('user', add_user, name='url_user_insert'),
  path('login', user_login, name='url_user_login'),
]
