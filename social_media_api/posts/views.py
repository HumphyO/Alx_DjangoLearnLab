from django.shortcuts import render, redirect
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment, Like, Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions, viewsets
from django.contrib import messages
from rest_framework.generics import get_object_or_404
from rest_framework import generics


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



def like_post(request, pk, generics):
    post = generics.get_object_or_404(Post, pk=pk)
    Like, created = Like.objects.get_or_create(user=request, post=post)
    if created:
         Notification.objects.create(
            recipient = post.author,
            actor = request.user,
            verb = 'You liked the post',
            target = post,
         )
         messages.success(request, 'You liked this post.')
         return redirect('post')



def unlike_post(request, pk, generics):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if like:
        like.delete()
        messages.success(request, 'You unliked This post')  

    else: 
        messages.warning(request, 'You have already liked the post')  
        
    
