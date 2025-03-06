from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, URLResolver
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns: list[URLResolver] = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='user')),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
