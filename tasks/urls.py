from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_tasks_list, name='get_tasks_list'),
    path('add/', views.add_task_form, name='add_task_form'),
    path('edit/<int:id>/', views.add_task_form, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]
