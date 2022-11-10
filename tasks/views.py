from django import forms
from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTask


def get_tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


def add_task_form(request):
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    else:
        form = AddTask()
        context = {
            'form': form
        }
        return render(request, 'tasks/add_task_form.html', context)
