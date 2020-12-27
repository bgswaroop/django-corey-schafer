from django.shortcuts import render

posts = [
    {
        'author': 'Guru Swaroop',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Dec 27, 2020'
    },
    {
        'author': 'Sukhmander Singh',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'Dec 27, 2020'
    }
]


def home(request):
    # The keys of the context will be accessible within the template
    context = {
        'posts': posts
    }
    # The following html page will be searched in the templates sub-directory within the blog app by django
    return render(request=request, template_name='blog/home.html', context=context)


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
