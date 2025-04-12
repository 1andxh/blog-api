from rest_framework import permissions
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from posts.models import Post
from rest_framework import status

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['GET', 'POST']

    @action(detail=True, methods=['POST'])
    def comment_add(self, request, pk):
        post = get_object_or_404(Post, pk=id)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['GET'])
    def comment_view(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        




