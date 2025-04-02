from django.core.cache import cache
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAutoRefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.path in ['/user/login/', '/user/register/', '/user/logout/']:
            return self.get_response(request)

        if '/admin/' in request.path:
            return self.get_response(request)

        if '/api/' in request.path:
            if request.headers.get('JS-Request') != 'True':
                return HttpResponseNotFound()
            else:
                return self.get_response(request)

        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return HttpResponseRedirect(f"{reverse('user:login')}?next={request.path}")

        try:
            jwt_authentication = JWTAuthentication()
            validated_token = jwt_authentication.get_validated_token(access_token)

            cache_key = f'user_{RefreshToken(refresh_token).get('user_id')}'

            if cache_value := cache.get(cache_key):
                print('Данные из кеша мидл')
                request.user = cache_value
            else:
                print('Данные из БД мидл')
                user = jwt_authentication.get_user(validated_token)
                cache.set(cache_key, user)
                request.user = user
        except (InvalidToken, TokenError):

            try:
                refresh = RefreshToken(refresh_token)
                access_token_new = str(refresh.access_token)

                jwt_authentication = JWTAuthentication()
                validated_token = jwt_authentication.get_validated_token(access_token_new)

                cache_key = f'user_{RefreshToken(refresh_token).get('user_id')}'

                if cache_value := cache.get(cache_key):
                    print('Данные из кеша мидл')
                    request.user = cache_value
                else:
                    print('Данные из БД мидл')
                    user = jwt_authentication.get_user(validated_token)
                    cache.set(cache_key, user)
                    request.user = user

                response = self.get_response(request)
                response.set_cookie(
                    key='access_token',
                    value=access_token_new,
                    httponly=True,
                    secure=True,
                    samesite='Strict',
                    max_age=3600,
                )

                return response
            except(InvalidToken, TokenError):
                return HttpResponseRedirect(f"{reverse('user:login')}?next={request.path}")

        return self.get_response(request)
