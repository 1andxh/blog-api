
from .models import Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer
from django.utils import timezone
# from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def post_view(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter(published__lte=timezone.now())
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def post_create(request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    # serializer.save(author=request.user)
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def post_detail(request, id):
    try:
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"message" : "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_by_tags(request):
    tags =request.query_params.get('tag')
    try:
        post = Post.objects.filter(tag__in=tags)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message" : f"No Post with tag(s) : {tags} found."})


@api_view(['PUT']) 
def post_update(request, id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return Response({"messsage" : "Post deleted."}, status=status.HTTP_204_NO_CONTENT)

