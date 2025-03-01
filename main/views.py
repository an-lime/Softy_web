from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render


def get_current_user(request):
    if request.method == 'GET':
        return HttpResponseNotFound()

    json_data = {
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username,
    }
    return JsonResponse(json_data)


@login_required
def index(request):
    return render(request, 'main/index.html')
