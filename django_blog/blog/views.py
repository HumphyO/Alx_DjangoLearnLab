from django.shortcuts import render, redirect
from django.contrib.auth import UserCreationForm
from django.contrib.auth import Login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, CustomUser, Comment
from .forms import CommentForm, ProfileForm, CreatePostForm
from .forms import Postforms, forms
from django.db.models import Q

# Create your views here.
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ['email',]


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

#Login View
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect ('logout.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance = request.user.profile)
        return render(request, 'edit_profile.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

# list View to display all blog posts
def PostListView(Listview):
    model = Post
    template_name = 'post_list.html'
    

# Detail View to show individual blog posts
def PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Create View to allow authenticated users to create new posts
def PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = Postforms
    template_name = 'post_create.html'
    success_url = '/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update View to enable authors to edit their posts
def PostUpdateView(LoginRequiredMixins, UserPassesTestMixins, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    
# Delete View to allow authors delete their posts
def PostDeleteView(LoginRequiredmixins, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/posts'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return post.author ==self.request.user


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author == self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'comment_update.html'

   

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'


def search_view(request):
    query = request.GET.get('q') 
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)|
            Q(tags__name__icontains=query)
        )
    else:
        posts = []
        
    context = {'posts': posts, 'query': query}
    return render(request, 'search_results.html')




