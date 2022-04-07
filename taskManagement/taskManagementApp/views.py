from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New item added!')
            return redirect('task_list')

    all_items = Task.objects.all()

    return render(request, 'task_list.html', {'all_items': all_items})


def delete(request, item_id):
    item = Task.objects.get(pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect('task_list')

@login_required
def tasks(request, task_pk):
    task = Task.objects.get(id=task_pk)

    return render(request, 'task.html', {'task': task})


def home(request):
    return render(request, 'home.html')
