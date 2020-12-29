from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

# It is advisable to use unique names for the paths
urlpatterns = [
    # An example of Class view
    path('', PostListView.as_view(), name='blog-home'),

    # An example of Function View
    path('about/', views.about, name='blog-about'),

    # An example where we are using the built-in identifiers of class view to create url patterns
    # here `pk` refers to primary-key. We can of course use any other name instead of `pk`, in which case we will
    # have to define that attribute inside the Class View
    # 'int:' is optional, if we know the type of `pk` then we can specify it here. This will prevent users to enter
    # any other value apart from an integer
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Create view
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Update view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')

]


# Notes:
# The class view PostListView.as_view() searches for the html template in the default location
# <app-name> / <model-name>_<view-name>.html
