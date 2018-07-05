from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoryForm, TaskForm

def new_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('Categoria adicionada com sucesso')
    else:
      print(form.errors)
  else:
    form = CategoryForm
  
  data = {}
  data['form'] = form
  return render(request, 'category/new.html', data)

def new_task(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('Tarefa adicionada com sucesso')
    else:
      print(form.errors)
  else:
    form = TaskForm
  
  data = {}
  data['form'] = form
  return render(request, 'task/new.html', data)  