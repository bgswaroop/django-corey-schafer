from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    # Note that the values in the context dictionary can be objects

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # to save the new user to our database
            form.save()
            # The cleaned data method returns a dictionary which contains the form inputs converted to python types
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You can now login!")

            # If the creation is successful then redirect the user to the blog-home page
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, template_name='users/register.html', context={'form': form})


@login_required()
def profile(request):
    return render(request, template_name='users/profile.html')
