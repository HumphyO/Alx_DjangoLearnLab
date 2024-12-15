from django.shortcuts import render, redirect
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment, Like, Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions, viewsets
from django.contrib import messages
from rest_framework.generics import get_object_or_404



# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user =self.request.user
        if user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(author=user)
    
    def feed (self, request):
        user = request.user
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user =self.request.user
        return Comment.objects.filter(author=user)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({'message': 'you are only allowed to edit your comments.'}, status=403)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({'message': 'you are only allowed to delete your comments.'}, status=403)
        return super().destroy(request, *args, **kwargs)



def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    if Like.object.filter(user=user, post=post).exists():
        f'(Warning, "You have liked this post.")'
        return redirect ('post_detail', post_id = post_id)
    
    like = Like.objects.create(user = user, post=post)

    notification = Notification.objects.create(
        recipient = post.author,
        actor = user,
        verb = 'liked',
        target = post,
    )
    messages.success(request, 'You liked this post.')
    return redirect('post_detail', post_id = post_id)

def unliked_post(request, post_id):
    post = get_object_or_404()
    user = request.user

    like, created = Like.objects.get_or_create(user = user, post=post)

    if like:
        like.delete()
        messages.success(request, 'You unliked Thi post')  

    else: 
        messages.warning(request, 'You have nit liked the psot')  
        return redirect('post_detail' , post_id=post_id)
    
