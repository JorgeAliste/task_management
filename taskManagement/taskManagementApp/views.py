from django.shortcuts import render
from .models import Task


# Create your views here.
def home(request):
    all_items = Task.objects.all()

    return render(request, 'index.html', {'all_items': all_items})
