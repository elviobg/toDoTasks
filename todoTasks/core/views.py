from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from todoTasks.tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
  data = {}
  data['tasks'] = get_list_or_404(Task)
  return render(request, 'index.html', data)