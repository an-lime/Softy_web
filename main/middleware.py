from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class TokenFromCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')
        request.access_token = access_token
        request.refresh_token = refresh_token
        response = self.get_response(request)
        return response


class JWTAutoRefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.path in ['/user/login/', '/user/register/', '/user/logout/']:
            return self.get_response(request)

        access_token = request.COOKIES.get('access_token')
        try:
            jwt_authentication = JWTAuthentication()
            validated_token = jwt_authentication.get_validated_token(access_token)
            user = jwt_authentication.get_user(validated_token)
            request.user = user
        except (InvalidToken, TokenError) as e:
            print('пора обновлять!!!')
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return JsonResponse({'error': 'Refresh token missing'}, status=401)

            try:
                print('начинаю обновлять!!!')
                refresh = RefreshToken(refresh_token)
                access_token_new = str(refresh.access_token)

                print(access_token)
                print(access_token_new)

                jwt_authentication = JWTAuthentication()
                validated_token = jwt_authentication.get_validated_token(access_token_new)
                user = jwt_authentication.get_user(validated_token)
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
                request.access_token = access_token_new
                print('обновил!!!')
                return response
            except(InvalidToken, TokenError) as e:
                return JsonResponse({'error': 'Invalid or expired refresh token'}, status=401)

        return self.get_response(request)
