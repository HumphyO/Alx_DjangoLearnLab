from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.decorators import user_passes_test, login_required 
from django.contrib.auth.decorators import permission_required


#Create Views here
#Function-based view
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'book': books})
@login_required
@permission_required('relationship_app.can_add_book')
def book_create(request): #Book creating logic
    return redirect('book_list')

@login_required
@permission_required('relationship_app.can_change_book')
def book_update(request, pk): #Updating a book logic
    return redirect('book_list')

@login_required
@permission_required('relationship_app.can_delete_book')
def book_delete(request, pk): #Deleting a book logic
    return redirect('book_list')
#Class_based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    


#login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')

        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

#Admin_view
def Admin_view(request):
    return render(request, 'admin_view.html', {'role': 'Admin'})

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

#Librarian_view
def Librarian_view(request):
    return render(request, 'librarian_view.html', {'role': 'Librarian'})

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

#Member_view
def Member_view(request):
    return render(request, 'member_view.html', {'role': 'Member'})

admin_view = user_passes_test(Admin_view)
librarian_view = user_passes_test(Librarian_view)
member_view = user_passes_test(Member_view)
