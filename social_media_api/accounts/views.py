from django.shortcuts import render
from rest_framework.response import response
from rest_framework.views import CreateAPIView, APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import TokenAPIView
from .models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

User = get_user_model

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)

class UserLoginAPIView(TokenAPIView):
    pass

class FollowUserView(APIView):
    def post (self, request, username):
        user_to_follow = get_object_or_404()(CustomUser, username= username)
        if user_to_follow ==request.user:
            return response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return response({'message': f'You are now following {username}.'}, status=status.HTTP_200_OK)
    
class UnfollowUserView(APIView):
    def post (self, request, username):
        user_to_follow = get_object_or_404()(CustomUser, username= username)
        if user_to_follow ==request.user:
            return response({'error': 'You cannot unfollow yourself.'}, status = status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return response({'message': f'You are now unfollowing {username}.'}, status=status.HTTP_200_OK)
        