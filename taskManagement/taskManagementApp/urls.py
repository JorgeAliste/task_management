from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.task_list, name='task_list'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('tasks/<int:task_pk>', views.tasks, name='task_page')
]
