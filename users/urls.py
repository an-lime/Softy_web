from django.urls import path, URLPattern
from users import views
from users.views import UserLoginView

app_name = 'users'
urlpatterns: list[URLPattern] = [

    # Вспомогательные методы для js
    path('get_current_user/', views.get_current_user, name='get_current_user'),

    # Основные пути
    path("login/", views.login, name="login"),
    path('api/login/', UserLoginView.as_view(), name='api_login'),

    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("profile/change/", views.profile_change, name="profile_change"),
    path("logout/", views.logout, name="logout"),
]
