from django.core.cache import cache
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')
        if not access_token:
            return None

        try:
            validated_token = self.get_validated_token(access_token)

            cache_key = f'user_{RefreshToken(refresh_token).get('user_id')}'
            if cache_value := cache.get(cache_key):
                print('Данные из кеша автоауф')
                user = cache_value
            else:
                print('Данные из БД автоауф')
                user = self.get_user(validated_token)

            return user, validated_token
        except Exception as e:
            raise AuthenticationFailed('Invalid token')
