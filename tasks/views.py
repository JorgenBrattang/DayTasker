from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTask


def get_tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


def add_task_form(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = AddTask(request.POST)
        else:
            task = Task.objects.get(pk=id)
            form = AddTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/tasks/')
    else:
        if id == 0:
            form = AddTask()
        else:
            task = Task.objects.get(pk=id)  # pk = primary key
            form = AddTask(instance=task)
        context = {
            'form': form
        }
        return render(request, 'tasks/add_task_form.html', context)


# def toggle_task(request, id):
#     task = Task.objects.get(pk=id)
#     task.done = not task.done
#     task.save()
#     return redirect('/tasks/')


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('/tasks/')
