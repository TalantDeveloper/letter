from django.shortcuts import render, redirect
from .models import Manager, CheckFile, ControlFile, Letter, Center
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .functions import content_need


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return redirect('admin/')
    return render(request, 'user/login.html')


@login_required
def welcome(request):
    content = content_need(request)
    return render(request, 'main/welcome.html', context=content)

