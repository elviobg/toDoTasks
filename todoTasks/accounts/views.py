from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib import messages

def add_user(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.set_password(user.password)
      user.save()
      return HttpResponse('usuario criado')
  else:
    form = UserForm()
    
  data = {}
  data['form'] = form
  return render(request, 'accounts/new.html', data)

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
      login(request, user)
      return redirect('url_home')
    else:
      messages.error(request, 'Usuário ou senha inválidos')
  
  return render(request, 'accounts/login.html')

