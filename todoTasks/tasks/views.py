from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import CategoryForm, TaskForm
from .models import Category, Task

def list_categories(request):
  data = {}
  data['categories'] = get_list_or_404(Category)
  return render(request, 'category/list.html', data)

def create_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()      
      return redirect('tasks:url_category')
    else:
      print(form.errors)
  else:
    form = CategoryForm
  
  data = {}
  data['form'] = form
  return render(request, 'category/new.html', data)

def create_task(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('url_home')
    else:
      print(form.errors)
  else:
    form = TaskForm
  
  data = {}
  data['form'] = form
  return render(request, 'task/new.html', data)

def delete_task(request, pk):
  get_object_or_404(Task, pk=pk).delete()
  return redirect('url_home')

def update_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':    
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('url_home')
    else:
      print(form.errors)
  else:
    form = TaskForm(instance=task)

  data = {}
  data['form'] = form
  return render(request, 'task/new.html', data)

def delete_category(request, pk):
  get_object_or_404(Category, pk=pk).delete()
  return redirect('tasks:url_category')

def update_category(request, pk):
  category = get_object_or_404(Category, pk=pk)
  if request.method == 'POST':    
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('tasks:url_category')
    else:
      print(form.errors)
  else:
    form = CategoryForm(instance=category)

  data = {}
  data['form'] = form
  return render(request, 'category/new.html', data)