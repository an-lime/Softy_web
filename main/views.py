from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from main.models import UserPost
from main.serializers import UserPostSerializer


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def index(request):
    return render(request, 'main/index.html')


# ==================================== #
# ===== Функции для работы с API ===== #
# ==================================== #

class PostViewSet(viewsets.ModelViewSet):

    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

    def list(self, request, *args, **kwargs):

        user_id = request.user.id
        last_date_time_str = request.query_params.get('lastDateTime')

        try:
            dt = datetime.fromisoformat(last_date_time_str)
            last_date_time = datetime.strptime(dt.strftime("%d-%m-%Y %H:%M:%S"), '%d-%m-%Y %H:%M:%S')
        except ValueError:
            last_date_time = datetime.strptime(last_date_time_str, '%d-%m-%Y %H:%M:%S')
        queryset = self.get_queryset()
        queryset = queryset.filter(created_at__lt=last_date_time).order_by('-created_at')[:8]
        serializer = self.get_serializer(queryset, many=True)

        # модификация данных
        post_data_modified = [
            {
                **post,
                'post_image': post['post_image'] or '',
                'post_date': post['created_at'],
                'is_author': post['author']['id'] == user_id
            }
            for post in serializer.data
        ]

        return JsonResponse({
            'posts': post_data_modified,
        })

    def create(self, request, *args, **kwargs):

        data_request = request.data.copy()
        data_request['created_at'] = timezone.now()

        serializer = self.get_serializer(data=data_request)
        if serializer.is_valid():
            serializer.save(author=request.user)
            data = serializer.data.copy()
            data['is_author'] = True
            return Response(data)
        else:
            return Response({'status': 'error'}, status=400)
