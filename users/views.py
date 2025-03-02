from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import Users


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def login(request):
    context = {}
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
            context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.user.is_authenticated:
        auth.logout(request)
    context = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))


# ==================================== #
# ===== Функции для работы с API ===== #
# ==================================== #

def get_current_user(request):
    if request.method == 'GET':
        return HttpResponseNotFound()

    if request.user.is_authenticated:
        current_user = Users.objects.get(pk=request.user.pk)
    else:
        return JsonResponse({'is_authenticated': request.user.is_authenticated})

    json_data = {
        'is_authenticated': request.user.is_authenticated,
        'first_name': current_user.first_name,
        'last_name': current_user.last_name,
        'avatar': current_user.avatar.url,
    }
    return JsonResponse(json_data)
