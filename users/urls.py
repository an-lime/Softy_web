from django.urls import path, URLPattern
from users import views

app_name = 'users'
urlpatterns: list[URLPattern] = [

    # Вспомогательные методы для js

    # Основные пути
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]
