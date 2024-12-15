from django.urls import path
from .views import MovieAPIView, ReviewCreateView, ReviewDetailView

urlpatterns = [
    path('movies/', MovieAPIView.as_view(), name='movie-list'),
    path('reviews/', ReviewCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'  )
]