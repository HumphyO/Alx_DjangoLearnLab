from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, like_post, unlike_post

router = DefaultRouter()

# Register PostViewSet and CommentViewSet 
router.register(r'posts', PostViewSet, basename= 'post')
router.register(r'comments', CommentViewSet, basename= 'comment')

urlpatterns = [
    path('api/', include ('posts.urls')),
    path('feed/', PostViewSet.as_view(), name='post_feed'),
    path('/posts/<int:pk>'),
    path('/posts/<int:pk>/like/', like_post.as_view(), name='like_post'),
    path('/posts/<int:pk>/unlike/', unlike_post.as_view(), name='unlike_post'),
]