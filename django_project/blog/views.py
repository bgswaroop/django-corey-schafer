from django.shortcuts import render
from .models import Post


def home(request):
    # The keys of the context will be accessible within the template
    context = {
        'posts': Post.objects.all()
    }
    # The following html page will be searched in the templates sub-directory within the blog app by django
    return render(request=request, template_name='blog/home.html', context=context)


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
