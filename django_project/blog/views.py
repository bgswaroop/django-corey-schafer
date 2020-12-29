from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    # The keys of the context will be accessible within the template
    context = {
        'posts': Post.objects.all()
    }
    # The following html page will be searched in the templates sub-directory within the blog app by django
    return render(request=request, template_name='blog/home.html', context=context)


class PostListView(ListView):
    # We need to create a variable model that will indicate the type of items in the list view
    model = Post

    # If this is not specified, the default location for the template will be searched.
    template_name = 'blog/home.html'  # <app-name> / <model-name>_<view-name>.html

    # Since html template is iterating over the name `posts`, we need to specify here that the name `posts`
    # refers to all the list of all Post(s).
    context_object_name = 'posts'

    # We can order the list items as follows: The '-' character in the beginning of the date_posted attribute
    # indicates to perform sorting in descending order.
    ordering = ['-date_posted']

    # Pagination
    paginate_by = 5


class PostDetailView(DetailView):
    # We need to create a variable model that will indicate the type of items in the list view
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # We need to create a variable model that will indicate the type of items in the list view
    model = Post
    fields = ['title', 'content']

    # The default behaviour for validating a form on submit. We will modify this method to set the author of the
    # post as the current user before validating it.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # We need to create a variable model that will indicate the type of items in the list view
    model = Post
    fields = ['title', 'content']

    # The default behaviour for validating a form on submit. We will modify this method to set the author of the
    # post as the current user before validating it.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This test method will prevent users from editing the posts of other users.
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # We need to create a variable model that will indicate the type of items in the list view
    model = Post

    # This test method will prevent users from deleting the posts of other users.
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # This is the page we need to redirect to once the post is deleted.
    success_url = '/'


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app-name> / <model-name>_<view-name>.html
    context_object_name = 'posts'
    paginate_by = 5

    # A filter to list posts only by a certain user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
