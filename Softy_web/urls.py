from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, URLResolver
from django.contrib import admin

urlpatterns: list[URLResolver] = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='user')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)