from rest_framework import serializers

from main.models import UserPost


class UserPostSerializer(serializers.ModelSerializer):
    post_text = serializers.CharField()
    post_image = serializers.ImageField(required=False)

    class Meta:
        model = UserPost
        fields = '__all__'
