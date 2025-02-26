from django.urls import path, URLPattern
from users import views

app_name = 'users'
urlpatterns: list[URLPattern] = [

    # Вспомогательные методы для js
    path("get_login_url/", views.get_login_url, name="get_login_url"),
    path("get_register_url/", views.get_register_url, name="get_register_url"),

    # Основные пути
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
]
