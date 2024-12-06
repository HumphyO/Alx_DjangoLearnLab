from django.shortcuts import render, redirect
from django.contrib.auth import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

# list View to display all blog posts
def PostListView(Listview):
    model = Post
    template_name = 'blog/blog_list.html'

# Detail View to show individual blog posts
def PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'pk'
    template_name = 'blog/blog_detail.html'

# Create View to allow authenticated users to create new posts
def PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/blog_create.html'

# Update View to enable authors to edit their posts
def PostUpdateView(LoginRequiredMixins, UserPassesTestMixins, UpdateView):
    model = Post
    pk_url_kwarg = 'pk'
    template_name = 'blog/blog_edit_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Delete View to allow authors delete their posts
def PostDeleteView(LoginRequiredmixins, UserPassesTestMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    template_name = 'blog/blog_delete_confirm.html'

    def test_func(self):
       post = self.get_object()
       return self.request.user == post.author






