from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

@login_required
def tasklist(request):
    status_filter = request.GET.get('status', 'all') 
    category_filter = request.GET.get('category', 'all')
    tasks = Task.objects.filter(user= request.user)

    if status_filter != 'all':
        tasks = tasks.filter(is_completed=(status_filter == 'completed'))
    if category_filter != 'all':
        tasks = tasks.filter(category= category_filter)

    completed_task = tasks.filter(is_completed= True)
    pending_task = tasks.filter(is_completed= False)

    return render(request, 'tasklist.html',{
        'completed_task': completed_task,
        'pending_task' : pending_task,
        'status_filter': status_filter,
        'category_filter': category_filter,
    })


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit= False)
            task.user = request.user
            task.save()
            return redirect('tasklist')
    else:
        form = TaskForm()
    return render(request, 'task_forms.html', {'form':form})

@login_required
def task_details(request, task_id):
    task = get_object_or_404(Task, id= task_id, user= request.user)

    return render(request, 'task_details.html', {'task':task})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id= task_id, user= request.user)
    task.delete()
    return redirect('tasklist')

@login_required
def task_mark_compeleted(request, task_id):
    task = get_object_or_404(Task,id=task_id,user=request.user)
    task.is_completed= True
    task.save()
    return redirect('tasklist')

def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('tasklist')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form':form})

# def user_logout(request):
#     logout(request)
#     return redirect('logout')