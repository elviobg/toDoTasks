from django.urls import path
from .views import add_user, user_login, user_logout

app_name = 'accounts'

urlpatterns = [
  path('accounts/add/', add_user, name='url_user_insert'),
  path('accounts/login/', user_login, name='url_user_login'),
  path('accounts/logout/', user_logout, name='url_user_logout'),
]
