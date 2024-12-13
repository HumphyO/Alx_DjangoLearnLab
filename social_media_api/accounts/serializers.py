from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token 

User = get_user_model

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True, read_only=True)
    following = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'bio', 'profile_picture', 'followers', 'following')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data)
        token , created = Token.objects.create(user = user)
        return user, token

class UserRegistartionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        User = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            bio = validated_data['bio'],
            profile_picture = validated_data['profile_picture', None]
        )

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']


