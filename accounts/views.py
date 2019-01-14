from django.shortcuts import render, redirect

from home.views import common_data
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from home.models import *
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        form = LoginForm(request.POST or None)
        context = common_data()
        context["header"] = GeneralHeader.objects.get(page_name='4')
        context["form"] = form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('home:index')
        return render(request, 'login/login.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        form = RegisterForm(request.POST or None)
        context = common_data()
        context["header"] = GeneralHeader.objects.get(page_name='6')
        context["form"] = form
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            # new_user = authenticate(username=user.username, password=password)
            # login(request, new_user)
            messages.success(request, 'Registration is successful!')

        return render(request, 'register_page/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("home:index")
