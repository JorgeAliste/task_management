from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New item added!')
            all_items = Task.objects.all()
            return render(request, 'index.html', {'all_items': all_items})

    all_items = Task.objects.all()

    return render(request, 'index.html', {'all_items': all_items})

def delete(request, item_id):
    item = Task.objects.get(pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect('home')
