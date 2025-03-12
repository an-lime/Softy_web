from django.urls import path, URLPattern
from users import views

app_name = 'users'
urlpatterns: list[URLPattern] = [

    # Вспомогательные методы для js
    path('get_current_user/', views.get_current_user, name='get_current_user'),

    # Основные пути
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]
