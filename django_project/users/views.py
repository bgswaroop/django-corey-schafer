from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


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

    # Note that by setting the instance we will be displaying the existing values in the forms
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Since the profile form also has an image input, therefore in addition to the request.POST data we also
        # need to pass the request.FILES
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')

            # Note that instead of falling back to the render(...) statement to show the profile page, we instead
            # redirect to the profile page. Why?
            # This is because on redirect we would perform a GET request (currently we are in a POST request)
            # Ok, lets say we do not perform the redirect, then the browser detects that we are attempting to load
            # a new page with the data already filled in the current page, and this might cause to lose the data.
            # Hence, the browser throws up a warning. To avoid this warning / pop-up we need to redirect.
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, template_name='users/profile.html', context=context)
