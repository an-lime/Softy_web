from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

def get_login_url(request):
    if request.method == "GET":
        return HttpResponseNotFound()

    login_url = reverse('user:login')
    return JsonResponse({'login_url': login_url})

def get_register_url(request):
    if request.method == "GET":
        return HttpResponseNotFound()

    register_url = reverse('user:register')
    return JsonResponse({'register_url': register_url})

def login(request):
    if request.user.is_authenticated:
        auth.logout(request)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.user.is_authenticated:
        auth.logout(request)
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))
