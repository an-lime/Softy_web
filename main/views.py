from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication


def index(request):
    return render(request, 'main/index.html')
