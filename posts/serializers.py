from rest_framework import serializers
from .models import Post
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from comments.serializers import CommentSerializer

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    comment = CommentSerializer(source='comments.all', many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title','content','created_at', 'modified', 'category', 'published', 'tag', 'comment']
    