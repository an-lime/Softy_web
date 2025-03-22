from django.urls import path, URLPattern, include
from rest_framework import routers

from main import views
from main.views import PostViewSet

app_name = 'main'
urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns += [
    path('', include(router.urls)),
]
