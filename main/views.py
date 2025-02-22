from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

@login_required
def index(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'main/index.html', context)