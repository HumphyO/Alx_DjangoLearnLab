from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()

# Register PostViewSet and CommentViewSet 
router.register(r'posts', PostViewSet, basename= 'post')
router.register(r'comments', CommentViewSet, basename= 'comment')
urlpatterns = [
    path('api/', include ('posts.urls')),
    path('feed/', PostViewSet.as_view(), name='post_feed'),
]