from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, FollowUserView, UnfollowUserView
urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name = 'register'),
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]