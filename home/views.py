from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def home_view(request):
    task_form = TaskForm()
    tasks = Task.objects.all()
    pending = Task.objects.filter(status='Pending').count()
    progress = Task.objects.filter(status='In Progress').count()
    complete = Task.objects.filter(status='Complete').count()
    context = {
        'task_form':task_form,
        'tasks':tasks,
        'pen':pending,
        'prog':progress,
        'com':complete,
    }
    return render(request,'home_view.html',context)

def create_task(request):
    task_form = TaskForm(request.POST or None)
    if task_form.is_valid():
        task_form.save()
        return redirect('home_view')
    return redirect('home_view')

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home_view')
