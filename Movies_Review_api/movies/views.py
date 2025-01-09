from .models import Review, User
from .serializers import ReviewSerializer, UserRegistrationSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, status 
from rest_framework.decorators import api_view

# Create your views here.

class ReviewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 12

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer =self.get_serializer(data=request.data)
        serializer.is_valid(raise_except=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserRegistrationSerializer(self.get_serializer_context()).data,
            "token": token.key                                  
        }, status=status.HTTP_201_CREATED)

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def create_review(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data) # Pass the data from the request into the serializer

         # Validate and save the serializer data if valid
        if serializer.is_valid():
            serializer.save() # Calls upon the 'create()' method of the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# API view to list all reviews for a specific movie or create a new review.
class ReviewList(ListCreateAPIView):
     queryset = Review.objects.all().order_by("created_date")
     serializer_class = ReviewSerializer
     permission_classes = [IsAuthenticated]
     pagination_class = ReviewPagination
     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
     search_fields = ['movie_title']
     ordering_fields = ['rating', 'created_date']

 # Allow POST requests with authentication for creating review   
@api_view(['POST'])
def create_review(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data) # Pass the data from the request into the serializer

        # Validate and save the serializer data if valid
        if serializer.is_valid():
            serializer.save() # Calls upon the 'create()' method of the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# API View to retrieve, update or delete a specific review instance 
class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        if self.action == 'retrieve':
            movie_title = self.request.get('movie_title')
            if movie_title:
                queryset = queryset.filter(movie_title=movie_title)
        return queryset


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response({"You are only allowed to edit your comment"}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
# Allows DELETE requests with authentication for deleting a view
    def destroy(self, request):
        instance = self.get_object()
        if instance.user != self.request.user:
            return Response({"You are only allowed to delete your reviews"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)



    
    




