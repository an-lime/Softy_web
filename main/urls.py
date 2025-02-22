from django.urls import path, URLPattern
from main import views

app_name = 'main'
urlpatterns: list[URLPattern] = [
    path("softy/", views.index, name="index"),
]