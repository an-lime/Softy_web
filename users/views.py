from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.forms import ProfileForm
from users.serializers import UserLoginSerializer, UserRegisterSerializer


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')


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

class AuthViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'user_id': user.id,
                'user_role': user.is_staff,
            })
            refresh_token = str(refresh)

            redirected_url = request.data.get('next', reverse('main:index'))

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

    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'user_id': user.id,
                'username': user.username,
            })

            redirected_url = reverse('users:login')
            response = Response({
                'redirected_url': redirected_url,
                'status_code': status.HTTP_201_CREATED,
            })
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
