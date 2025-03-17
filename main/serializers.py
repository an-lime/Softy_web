from rest_framework import serializers

from main.models import UserPost


class UserNewPostSerializer(serializers.ModelSerializer):
    post_text = serializers.CharField()
    post_image = serializers.ImageField(required=False)

    class Meta:
        model = UserPost
        fields = ('post_text', 'post_image', 'author')
