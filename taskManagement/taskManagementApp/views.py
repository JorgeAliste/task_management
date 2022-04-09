from django.core.exceptions import PermissionDenied
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
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'New item added!')
            return redirect('task_list')

    all_items = Task.objects.filter(user=request.user)

    return render(request, 'task_list.html', {'all_items': all_items})


def delete(request, item_id):
    item = Task.objects.get(pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect('task_list')


@login_required
def tasks(request, task_pk):
    task = Task.objects.get(id=task_pk)

    if request.user == task.user:

        if request.method == 'POST':
            if 'change_status' in request.POST:
                task.completed = not task.completed
                task.save()

        return render(request, 'task.html', {'task': task})
    else:
        raise PermissionDenied()


def home(request):
    return render(request, 'home.html')
