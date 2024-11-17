from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def librarian_view(request):
    return render(request, 'librarian_view.html', {'role': 'Librarian'})

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

# Librarian_only view
@user_passes_test
def librarian_view(requset):
    context = {
        'role': 'Librarian'
    }
    return render (requset, 'relationship_app/librarian_vew.html', context)