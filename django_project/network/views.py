from django.shortcuts import render
from .models import Network


# Create your views here.
def home(request):
    context = {
        'network': Network.objects.all()
    }
    return render(request=request, template_name='network/home.html', context=context)
