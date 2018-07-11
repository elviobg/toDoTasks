from django.urls import path
from .views import add_user

app_name = 'accounts'

urlpatterns = [
  path('user', add_user, name='url_user_insert'),
]
