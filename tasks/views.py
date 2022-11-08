from django.shortcuts import render
from .models import Task


def get_tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)
