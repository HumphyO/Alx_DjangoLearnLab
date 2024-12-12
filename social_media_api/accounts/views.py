from django.shortcuts import render
from rest_framework.response import response
from rest_framework.views import CreateAPIView
from rest_framework.generics import permissions
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import TokenAPIView
# Create your views here.

User = get_user_model

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)

class UserLoginAPIView(TokenAPIView):
    pass