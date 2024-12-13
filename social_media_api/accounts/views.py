from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import CreateAPIView, APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import TokenAPIView
from .models import CustomUser
from rest_framework import viewsets


# Create your views here.

User = get_user_model

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)

class UserLoginAPIView(TokenAPIView):
    pass


class UserViewSet(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_classes = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def follow(self, request):
        user = self.request.user
        to_follow = self.get.object
        user.followers.add(to_follow)
        return Response({'message': 'Successfully followed User.'})
        
    
    def unfollow(self, request):
        user = self.request.user
        to_unfollow = self.get_object()
        user.followers.remove(to_unfollow)
        return Response({'message': 'User successfully unfollowed.'})