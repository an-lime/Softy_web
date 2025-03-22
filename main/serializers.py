from rest_framework import serializers

from main.models import UserPost
from users.serializers import UserSerializer


class UserPostSerializer(serializers.ModelSerializer):
    post_text = serializers.CharField()
    post_image = serializers.ImageField(required=False)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    author = UserSerializer(read_only=True)

    class Meta:
        model = UserPost
        fields = '__all__'