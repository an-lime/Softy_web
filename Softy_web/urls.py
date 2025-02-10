from django.urls import path, include, URLResolver
from django.contrib import admin

urlpatterns: list[URLResolver] = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='user')),
]