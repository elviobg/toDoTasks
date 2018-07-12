from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserForm
from django.contrib import messages

def add_user(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():      
      form.save()
      return redirect('url_home')
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
      return redirect(request.GET.get('next', '/'))
    else:
      messages.error(request, 'Usuário ou senha inválidos')
  
  return render(request, 'accounts/login.html')

def user_logout(request):
  logout(request)
  return redirect('accounts:url_user_login')

def user_edit(request):
  if request.method == 'POST':
    formPassword = PasswordChangeForm(request.user, request.POST)
    if formPassword.is_valid():
      user = formPassword.save()
      update_session_auth_hash(request, user)
      messages.success(request, "Senha alterada com sucesso!")        
  else:
    formPassword = PasswordChangeForm(request.user)    

  data = {}
  data['form'] = formPassword  
  return render(request, 'accounts/edit.html', data)