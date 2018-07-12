from django.shortcuts import render, HttpResponse
from .forms import UserForm

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


