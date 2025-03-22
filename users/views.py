from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from users.serializers import UserAuthSerializer


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def login(request):
    return render(request, 'users/login.html')


# def login(request):
#     context = {}
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#
#             if user:
#                 refresh = RefreshToken.for_user(user)
#                 refresh.payload.update({
#                     'user_id': user.id,
#                     'user_role': user.is_staff,
#                 })
#                 refresh_token = str(refresh)
#
#                 if request.POST.get('next', None):
#                     response = HttpResponseRedirect(request.POST.get('next'))
#                 else:
#                     response = HttpResponseRedirect(reverse('main:index'))
#
#                 response.set_cookie(
#                     key='refresh_token',
#                     value=refresh_token,
#                     httponly=True,
#                     secure=True,
#                     samesite='Strict',
#                     max_age=86400,
#                 )
#
#                 return response
#
#         else:
#             context = {'form': form}
#     return render(request, 'users/login.html', context)


def register(request):
    context = {}

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
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


def profile_change(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/profile_change.html')


def logout(request):
    response = HttpResponseRedirect(reverse('user:login'))
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response


# ==================================== #
# ===== Функции для работы с API ===== #
# ==================================== #

class UserLoginView(APIView):
    def get(self, request):
        if request.headers.get('JS-Request') != 'True':
            return HttpResponseNotFound()

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'user_id': user.id,
                'user_role': user.is_staff,
            })
            refresh_token = str(refresh)

            redirected_url = request.data.get('next', reverse('main:index'))
            print(redirected_url)

            response = Response({
                'redirected_url': redirected_url,
                'status_code': status.HTTP_200_OK,
            })

            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='Strict',
                max_age=86400,
            )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_current_user(request):
    if request.headers.get('JS-Request') != 'True':
        return HttpResponseNotFound()

    if not request.user.is_authenticated:
        return JsonResponse({'is_authenticated': request.user.is_authenticated})

    json_data = {
        'user_id': request.user.id,
        'is_authenticated': request.user.is_authenticated,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'avatar': request.user.avatar.url,
    }
    return JsonResponse(json_data)
