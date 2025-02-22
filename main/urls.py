from django.urls import path, URLPattern
from main import views

app_name = 'main'
urlpatterns: list[URLPattern] = [

    path('get_current_user/', views.get_current_user, name='get_current_user'),
    path("", views.index, name="index"),
]