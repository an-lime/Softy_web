from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class UserAuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            email="test@example.com"
        )
        self.login_url = "/user/api/auth/login/"

    def test_successful_login(self):
        """ Авторизация по верным данным """
        data = {
            "username": "testuser",
            "password": "testpass123",
        }
        response = self.client.post(self.login_url, data, headers={
            'JS-Request': 'True'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_password_login(self):
        """ Попытка авторизации по неверным данным """
        data = {
            "username": "testuser",
            "password": "wrongpass",
        }
        response = self.client.post(self.login_url, data, headers={
            'JS-Request': 'True'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
