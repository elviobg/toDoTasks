from django.urls import path
from .views import add_user, user_login, user_logout

app_name = 'accounts'

urlpatterns = [
  path('user', add_user, name='url_user_insert'),
  path('login', user_login, name='url_user_login'),
  path('logout', user_logout, name='url_user_logout'),
]
