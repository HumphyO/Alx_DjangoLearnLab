from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = {
    path('login/', views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile_view, name = 'profile'),
    path('/posts/', views.PostListView.as_view(), name = 'post_list'),
    path('post/new/', views.PostCreateView.as_view(), name = 'post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post_delete'),
    path('/comment/<int:post_id>/comments/new/', views.CommentListView.as_view(), name = 'post-comments'),
    path('/comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name = 'comment_update'),
    path('/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name = 'comment_delete'),
}