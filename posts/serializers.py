from rest_framework import serializers
from .models import Post
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    class Meta:
        model = Post
        fields = ['id', 'title','content','created_at', 'modified', 'category', 'published', 'tag']
    