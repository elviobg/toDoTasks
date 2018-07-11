from django.shortcuts import render, HttpResponse
from .forms import UserForm

def add_user(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('usuario criado')
  else:
    form = UserForm()
    
  data = {}
  data['form'] = form
  return render(request, 'accounts/new.html', data)


