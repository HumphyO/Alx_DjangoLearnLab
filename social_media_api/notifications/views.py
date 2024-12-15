from django.shortcuts import render, redirect
from.models import Post, Like, Notification
from django.contrib import messages
from django.views.generic import ListView

# Create your views here.

def like_post(request, post_id):
    post = post_id.get.objects.all()
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
    post = Post.get_object_all()
    user = request.user

    like = Like.objects.create(user = user, post=post)

    if like:
        like.delete()
        messages.success(request, 'You unliked Thi post')  

    else: 
        messages.warning(request, 'You have nit liked the psot')  
        return redirect('post_detail' , post_id=post_id)
    
class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_list.html'

    def get_queryset(self):
        return self.request.user.notifications.order_by('-timestamp')