from django.urls import path
from .views import ReviewList, ReviewDetail, UserList, UserDetail,MovieRecommendationview



urlpatterns = [
    path('users/', UserList.as_view(), name=''),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
    path('recommendations', MovieRecommendationview.as_view(), name = "movie-recommendations"),
]