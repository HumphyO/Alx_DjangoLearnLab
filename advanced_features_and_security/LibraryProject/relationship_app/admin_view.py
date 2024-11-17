from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.profile_role == 'Admin'

@user_passes_test(is_admin)
#Admin_view
def admin_view(request):
    context = {
        'role': 'Admin',
    }
    return render(request, 'relationship/admin_view.html', {'role': 'Admin'})