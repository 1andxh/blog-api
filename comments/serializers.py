from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id'
            'author',
            'post',
            'content',
            'timestamp'
        ]

# anyone can see it and do crud