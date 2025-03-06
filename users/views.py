from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import result
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import Users


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def login(request):
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                refresh.payload.update({
                    'user_id': user.id,
                    'user_role': user.is_staff,
                })
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                if request.POST.get('next', None):
                    response = HttpResponseRedirect(request.POST.get('next'))
                else:
                    response = HttpResponseRedirect(reverse('main:index'))

                response.set_cookie(
                    key='access_token',
                    value=access_token,
                    httponly=True,
                    secure=True,
                    samesite='Strict',
                    max_age=3600,
                )
                response.set_cookie(
                    key='refresh_token',
                    value=refresh_token,
                    httponly=True,
                    secure=True,
                    samesite='Strict',
                    max_age=86400,
                )

                return response

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
            user = form.save()

            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'user_id': user.id,
                'username': user.username,
            })

            return HttpResponseRedirect(reverse('users:login'))

    return render(request, 'users/register.html', context)


def profile(request):
    return render(request, 'users/profile.html')


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
