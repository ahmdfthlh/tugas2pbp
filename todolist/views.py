from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_of_task': data_todolist,
    }

    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def create_task(request):
    if request.method == "POST":
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        add_task = Task(
            user = request.user,
            title = judul,
            description = deskripsi,
        )
        add_task.save()
        return redirect('todolist:show_todolist')        
    return render(request, 'create_task.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def delete(request, name):
    get_todo = Task.objects.get(user=request.user, title=name)
    get_todo.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def update(request, name):
    get_todo = Task.objects.get(user=request.user, title=name)
    get_todo.status = True
    get_todo.save()
    return redirect('todolist:show_todolist')

# REFERENSI DELETE & UPDATE TASK
# link: https://youtu.be/hWAF_WRs-iI
