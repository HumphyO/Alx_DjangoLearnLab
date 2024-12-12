from .models import Post, Comment
from rest_framework import serializers
from accounts.models import CustomUser # Import CustomUser Model
from rest_framework.validators import UniqueValidator




class  CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
        validators = [
            UniqueValidator(queryset = Comment.objects.all, message="You can't have duplicate comments!")
        ]

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

        def validate_title(self,value):
            if len(value) < 5:
                raise serializers.ValidationError("Title must be at least 5 characters long.")
            return value