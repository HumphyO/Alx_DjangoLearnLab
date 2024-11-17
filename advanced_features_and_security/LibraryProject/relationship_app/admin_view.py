from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_admin(user):
    return user.profile_role == 'Admin'

@user_passes_test(user_is_admin)
#Admin_view
def admin_view(request):

    return render(request, 'relationship_app/admin_view.html')

admin_view = user_passes_test(user_is_admin)(admin_view)