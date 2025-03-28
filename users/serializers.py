from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'avatar']


class UserLoginSerializer(serializers.ModelSerializer):
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
        fields = ('username', 'password')


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password_error': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        validated_data['password'] = validated_data.get('password1')
        validated_data.pop('password1')
        validated_data.pop('password2')
        user = Users.objects.create_user(**validated_data)
        return user
