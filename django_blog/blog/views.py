from django.shortcuts import render, redirect
from django.contrib.auth import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

#Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            form.add_error(None, 'Invalid username or password')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    #Redirects to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

#Logout View
def logout_view(request):
    logout(request)
    return redirect('profile')

#Profile view
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST
        user.save()
        return redirect('profile')
    return render(request, 'profile.html')