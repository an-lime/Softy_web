from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from environs import ValidationError
from rest_framework import serializers

from users.models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name']

class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError('Неверные введённые данные')
        else:
            raise serializers.ValidationError('Поля не заполнены')
        return data

    class Meta:
        model = Users
        fields = ['username', 'password']