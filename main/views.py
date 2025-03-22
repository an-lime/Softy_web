from datetime import datetime
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import UserPost
from main.serializers import UserPostSerializer
from users.authentication import CustomJWTAuthentication


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def index(request):
    return render(request, 'main/index.html')


# ==================================== #
# ===== Функции для работы с API ===== #
# ==================================== #

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

    def list(self, request, *args, **kwargs):
        if request.headers.get('JS-Request') != 'True':
            return HttpResponseNotFound()

        last_date_time_str = request.query_params.get('lastDateTime')
        last_date_time = datetime.strptime(last_date_time_str, '%d-%m-%Y %H:%M:%S')
        queryset = self.get_queryset()
        queryset = queryset.filter(created_at__lt=last_date_time).order_by('-created_at')[:8]
        serializer = self.get_serializer(queryset, many=True)

        # модификация данных
        post_data_modified = []
        for post in serializer.data:
            post_data = dict(post)
            post_data['author_name'] = post['author']['first_name']
            post_data['author_surname'] = post['author']['last_name']
            post_data['author_ref'] = post['author']['id']
            post_data['post_image'] = post['post_image'] if post['post_image'] else ''
            post_data['post_date'] = post['created_at']
            post_data['is_author'] = True if post['author']['id'] == request.user.id else False
            post_data_modified.append(post_data)

        return JsonResponse({
            'posts': post_data_modified,
        })

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author'] = request.user.id

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data.copy()
            data['is_author'] = True
            return Response(data)
        else:
            return Response({'status': 'error'}, status=400)
