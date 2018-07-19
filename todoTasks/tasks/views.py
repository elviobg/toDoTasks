from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, TaskForm
from .models import Category, Task

@login_required
def list_categories(request):
  data = {}
  data['categories'] = Category.objects.filter(user=request.user)
  return render(request, 'category/list.html', data)

@login_required
def create_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      category = form.save(commit=False)
      category.user = request.user
      category.save()
      return redirect('tasks:url_category')
    else:
      print(form.errors)
  else:
    form = CategoryForm
  
  data = {}
  data['form'] = form
  return render(request, 'category/new.html', data)

@login_required
def create_task(request):
  if request.method == 'POST':
    form = TaskForm(user=request.user, data=request.POST)
    if form.is_valid():      
      task = form.save(commit=False)
      task.user = request.user
      task.save()
      return redirect('url_home')
    else:
      print(form.errors)
  else:
    form = TaskForm(user=request.user)
  
  data = {}
  data['form'] = form
  return render(request, 'task/new.html', data)

@login_required
def delete_task(request, pk):  
  #Task.objects.filter(pk=pk, user=request.user).delete()
  task = get_object_or_404(Task, pk=pk, user=request.user)
  task.delete()
  return redirect('url_home')

@login_required
def delete_category(request, pk):
  #Category.objects.filter(pk=pk, user=request.user).delete()
  category = get_object_or_404(Category, pk=pk, user=request.user)
  category.delete()
  return redirect('tasks:url_category')

@login_required
def update_task(request, pk):
  task = get_object_or_404(Task, pk=pk, user=request.user)  
  if request.method == 'POST':    
    form = TaskForm(user=request.user, data=request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('url_home')
    else:
      print(form.errors)
  else:
    form = TaskForm(user=request.user, instance=task)

  data = {}
  data['form'] = form
  return render(request, 'task/new.html', data)

@login_required
def update_category(request, pk):  
  category = get_object_or_404(Category, pk=pk, user=request.user)
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