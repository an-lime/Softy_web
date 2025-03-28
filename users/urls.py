from django.urls import path, URLPattern, include
from rest_framework import routers

from users import views

app_name = 'users'

# роутеры
router_auth = routers.DefaultRouter()
router_user = routers.DefaultRouter()
router_auth.register(r'auth', views.AuthViewSet, basename='auth')
router_user.register(r'users', views.UserViewSet, basename='users')
urlpatterns: list[URLPattern] = [

    # Основные пути
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/change/", views.profile_change, name="profile_change"),
    path("profile/<user_id>/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]

urlpatterns += [

    # Запросы к api
    path('api/', include(router_auth.urls)),
    path('api/', include(router_user.urls)),
]
