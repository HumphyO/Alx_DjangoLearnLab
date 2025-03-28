from .models import Review, User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email", "first_name", "last_name")

        def validate(self, attrs):
            if attrs["password"] != attrs["password2"]:
                raise serializers.ValidationError({"password": "Passwords fields don't match."})
            return attrs

        def create(self, validate_data):
            user = Token.objects.create_user(
                username = validate_data["username"],
                email = validate_data["email"],
                password= validate_data["password"],
                first_name= validate_data["first_name"],
                last_name= validate_data["last_name"]
            )
            user.set_password(validate_data["password"])
            return User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email") 


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['user_id', 'movie_title', 'review_content', 'rating', 'created_date']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating should be between 1 to 5.")
        return value
       

       
class MovieRecommendationSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField()