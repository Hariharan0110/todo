from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    comepleted_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'completed_tasks': comepleted_tasks
    }
    return render(request, 'home.html', context)