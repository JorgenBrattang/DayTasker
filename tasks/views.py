from django.shortcuts import render, redirect
from .models import Task


def get_tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        done = 'done' in request.POST
        Task.objects.create(name=name, done=done)
        return redirect('get_tasks_list')
    return render(request, 'tasks/add_task.html')
