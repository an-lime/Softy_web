from django.urls import path, URLPattern, include
from rest_framework import routers

from users import views

app_name = 'users'

router_auth = routers.DefaultRouter()
router_auth.register(r'auth', views.AuthViewSet, basename='auth')
urlpatterns: list[URLPattern] = [

    # Вспомогательные методы для js
    path('get_current_user/', views.get_current_user, name='get_current_user'),
    path('api/', include(router_auth.urls)),

    # Основные пути
    path("login/", views.login, name="login"),

    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("profile/change/", views.profile_change, name="profile_change"),
    path("logout/", views.logout, name="logout"),
]
