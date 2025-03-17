from django.core.paginator import Paginator
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
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'}, status=400)

class GetPostView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.headers.get('JS-Request') != 'True':
            return HttpResponseNotFound()

        posts_all = UserPost.objects.all().order_by('-created_at')
        paginator = Paginator(posts_all, 6)
        page = request.GET.get('page')
        post_page = paginator.page(page)
        posts_data = [{'author_name': post.author.first_name,
                    'author_surname': post.author.last_name,
                    'author_ref': post.author.id,
                    'post_text': post.post_text,
                    'post_image': post.post_image.url if post.post_image else '',
                    'post_date': post.created_at.strftime('%d-%m-%Y')} for post in post_page]

        return JsonResponse({
            'posts': posts_data,
            'has_next': post_page.has_next()
        })