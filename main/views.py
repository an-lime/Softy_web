import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.forms import AddNewPostForm
from main.serializers import UserPostSerializer


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def index(request):
    return render(request, 'main/index.html')


# ==================================== #
# ===== Функции для работы с API ===== #
# ==================================== #

class AddNewPostView(APIView):

    def post(self, request):

        data = request.data.copy()

        serializer = UserPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            print(serializer.errors)
            return Response({'status': 'error', 'errors': serializer.errors}, status=400)

# def add_new_post(request):
#     if request.method == 'POST':
#         form = AddNewPostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             print("Валид")
#             print(form.cleaned_data)
#             # form.save()
#         else:
#             print("Не валид")
#             print(form.cleaned_data)
#             print(form.errors)
#     return JsonResponse({"status": "success"})
