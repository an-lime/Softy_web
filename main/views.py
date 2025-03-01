from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'main/index.html')
