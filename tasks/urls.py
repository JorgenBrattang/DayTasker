from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_tasks_list, name='get_tasks_list'),
    path('add/', views.add_task_form, name='add_task_form')
]
