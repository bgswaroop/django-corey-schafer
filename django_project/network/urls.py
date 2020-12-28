from django.urls import path
from . import views

# It is advisable to use unique names for the paths
urlpatterns = [
    path('', views.home, name='network-home')
]
