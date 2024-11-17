from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def member_view(request):
    return render(request, 'librarian_view.html', {'role': 'Member'})

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

# Librarian_only view
@user_passes_test
def member_view(requset):
    context = {
        'role': 'Member'
    }
    return render (requset, 'relationship_app/member_vew.html', context)