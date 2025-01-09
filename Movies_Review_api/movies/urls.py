from django.urls import path
from .views import ReviewList, ReviewDetail, UserList, UserDetail



urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view())
]