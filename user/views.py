from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    serializer =UserSerializer(instance=user)
    if not user.check_password(request.data['password']):
        return Response({"message" : "username or password is incorrect"}, status=status.HTTP_404_NOT_FOUND)
    token, create = Token.objects.get_or_create(user=user)
    print(f"TOKEN: {token}")
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        print(f"TOKEN: {token}")
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([SessionAuthentication, TokenAuthentication])
# @authentication_classes([IsAuthenticated])
# def get_token(request):
#     return Response("Authorized User {}".format(request.user.username))