from django import forms
from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
from django.http import JsonResponse

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
    print(request.POST)
    if task_form.is_valid():
        obj = task_form.save()
        data = Task.objects.values().get(id=obj.id)
        return JsonResponse({'status':'success','data':data})
    return JsonResponse({'status':'fail'})

def delete_task(request):
    id = request.GET['sid']
    task = Task.objects.get(id=id)
    task.delete()
    return JsonResponse({'status':'success','task_status': task.status})
