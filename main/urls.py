from django.urls import path, URLPattern, include
from rest_framework import routers

from main import views
from main.views import PostViewSet

app_name = 'main'

# роутеры
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

# Основные пути
urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]

# Запросы к api
urlpatterns += [
    path('api/', include(router.urls)),
]
