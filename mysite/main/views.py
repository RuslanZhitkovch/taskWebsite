from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task



def index(request):

    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    tasks = Task.objects.all()
    return render(request,'main/tasks.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})

def createTask(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks')
        else:
            error = 'Ошибка 404. Форма была некорректной.'

    form = TaskForm()
    context = {

        'form' : form,
        'eror' : error

    }
    return render(request, 'main/createTask.html',context)