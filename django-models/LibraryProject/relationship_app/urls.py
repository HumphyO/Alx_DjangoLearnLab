from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns =[   
     path('books/', list_books, name='list_books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name = 'library_detail'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', name='login')),
    path('admin/', views.admin_view, name = 'admin_view'),
    path('librarian/', views.librarian_view, name = 'librarian_view'),
    path('member/', views.member_view, name = 'member'),
    path('create/', views.add_book, name = 'add_book'),
    path('update/', views.book_update, name = 'book_update'),
    path('delete/', views.book_delete, name = 'book_delete'),
    ]
    
