from datetime import datetime
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import UserPost
from main.serializers import UserNewPostSerializer
from users.authentication import CustomJWTAuthentication


# =============================================== #
# ===== Функции, возвращающие HTML страницу ===== #
# =============================================== #

def index(request):
    return render(request, 'main/index.html')


# ==================================== #
# ===== Функции для работы с API ===== #
# ==================================== #

class AddNewPostView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return HttpResponseNotFound()

    def post(self, request):
        data = request.data.copy()
        data['author'] = request.user.id

        serializer = UserNewPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data.copy()
            data['is_author'] = True
            return Response(data)
        else:
            return Response({'status': 'error'}, status=400)


class GetPostView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.headers.get('JS-Request') != 'True':
            return HttpResponseNotFound()

        last_date_time_str = request.GET.get('lastDateTime')
        last_date_time = datetime.strptime(last_date_time_str, '%d-%m-%Y %H:%M:%S')

        posts_all = UserPost.objects.all().filter(created_at__lt=last_date_time).order_by('-created_at')[:8]
        posts_data = [{'id': post.id,
                       'author_name': post.author.first_name,
                       'author_surname': post.author.last_name,
                       'author_ref': post.author.id,
                       'post_text': post.post_text,
                       'post_image': post.post_image.url if post.post_image else '',
                       'post_date': post.created_at.strftime('%d-%m-%Y %H:%M:%S'),
                       'is_author': True if post.author.id == request.user.id else False} for post in posts_all]

        return JsonResponse({
            'posts': posts_data,
        })
