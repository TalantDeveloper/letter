from django.shortcuts import render, redirect
from .models import Manager, CheckFile, ControlFile, Letter, Center
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .functions import content_need, manager_today, manager_control_file, manager_out, get_models_list


def login_view(request):
    if request.method == 'POST':
        print("Post")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            print("Kirdi")
            login(request, user)
            return redirect("main:welcome")
        else:
            return redirect('main:login')
    return render(request, 'user/login.html')


@login_required
def welcome(request):
    content = content_need(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def today_view(request):
    content = manager_today(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def finish_view(request):
    content = manager_control_file(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def manager_out_view(request):
    content = manager_out(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def create_manager_view(request):
    content = get_models_list(request)
    if request.method == 'POST':
        print("Post")

    return render(request, 'main/home_create.html', context=content)







