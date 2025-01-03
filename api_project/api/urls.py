from django.urls import path, include
from views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'book_all')

urlpatterns = [
    # Route for BookList view(ListAPIView)
    path('books/', BookList.as_view(), name = 'book-list'), # Map to the BookList view

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)), # Includes all routes registered with the router
]