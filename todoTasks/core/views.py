from django.shortcuts import render
from django.http import HttpResponse
from todoTasks.tasks.models import Task

# Create your views here.
def home(request):
  data = {}
  data['tasks'] = Task.objects.all()
  return render(request, 'index.html', data)