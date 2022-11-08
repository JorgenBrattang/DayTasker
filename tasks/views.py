from django.shortcuts import render


def get_tasks_list(request):
    return render(request, 'tasks/tasks_list.html')
