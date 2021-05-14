from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.form import CreateUserForm, TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')

    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited!"))
        return redirect('todolist')

    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')

@login_required(login_url='login')
def index(request):
    context = {
        'index_text':"witaj na stronie głownej",
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'contact_text':"witaj na stronie kontaktowej",
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':"O mnie",
    }
    return render(request, 'about.html', context)


def files(request):
    context = {
        'files_text':"repozytorium plików",
    }
    return render(request, 'files.html', context)

def portfolio(request):
    context = {
        'portfolio_text':"portfolio",
    }
    return render(request, 'portfolio.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist')

        else:
            messages.info(request, 'Username OR password is incorect')

    context = {'login_text':"login", }
    return render(request, 'login.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Was created for' + user )
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
