# Follow on Django Tutorials - Corey Schafer

---

**DISCLAIMER**: This file is not intended to be a readme file. This document is 
for a quick reference to the django cmd commands covered in the course. For a full tutorial kindly refer 
to the video lectures - https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer

#### Part 1: Create a django project

    # lists all the available commands 
    djamgo-admin 
    
    # start the project
    django-admin startproject django_project

Note: Further commands will be executed from within the `djano_project` directory.

    # python manage.py runserver
    # First time this throws warnings for unapplied migrations, but that is okay. We will fix it later.

#### Part 2: Applications and Routes

Applications are independent of the django_project. A project can have several applications. 
Applications can be easily ported from one project to another. 
    
    # Create a new application
    python manage.py startapp blog

To install an app into the current project add an appropriate entry in the settings.py file of the project

#### Part 3: Templates and CSS

- https://getbootstrap.com/docs/4.3/getting-started/introduction/


#### Part 4: Admin page
Go to : localhost:8080/admin

    # First time this throws up error
    python manage.py createsuperuser

    # We need to first create a database, to store the details of the users. 
    # For that we first need to run migrations
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

#### Part 5: Databases and Migrations

Django allows us to create our own ORMs. These database structures are called as models. 
Refer to models.py file within the application directory

    # After defining the model class within the models.py file.  
    # This command will create the migrate code inside the migration sub-directory    
    python manage.py makemigrations
    
    # Using the app name and migration number, we can run the sql command to create a table
    python manage.py sqlmigrate blog 0001

    # Now, the above changes will get reflected into the database
    python manage.py migrate


To show the app in the admin page, register the app in the `admin.py` file of the app.


#### Part 6: Forms

Use pre-defined forms in Django

    from django.contrib.auth.forms import UserCreationForm

Modify these forms by inheriting from them as shown in the file `users/forms.py` 

A very commonly used library for forms is *crispy forms*. Add the application entry in the settings.py and 
also add the line `CRISPY_TEMPLATE_PACK = 'bootstrap4'` to the end of this file. This command will override the default `bootstrap2` which is outdated at this 
moment.

In the base html template add the line `{% load crispy_forms_tags %}` and style the forms by using `{{ form|crispy }}` in the corresponding html template. 


#### Part 7: Login and Logout System

Instead of writing our own views, we now use the Django inbuilt views for login and logout.
To do this we need to import `django.contrib.auth.views` by providing appropriate path to the html template.
For instance, we can modify the `urls.py` project file with the following lines:

    from django.contrib.auth import views as auth_views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

We can change the default behaviour of login view, by setting a few globals. For example,
the login view redirects the users to their profile page upon successful creation. We can change 
this by instead redirecting users to the `blog-home` page, by appending the following code
snippet to the `settings.py` file:  

    LOGIN_REDIRECT_URL = 'blog-home'

When users try to access certain pages that require authentication, then such views can be
decorated using the built-in decorator `from django.contrib.auth.decorators import login_required`
Note that, we will have to also change the default route for the log-in page in this decorator.
This can be achieved by setting the global variable in the `settings.py` file:

    LOGIN_URL = 'login'

#### Part 8: User Profiles and Pictures

User profiles can be created by creating a model with OneToOne mapping of the username.
The media content can be uploaded to a specific location in the project. To do this we will have to 
specify their location in the `settings.py` file:

    # For performance reasons, media files are stored on the file system and not in the database
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

Once the Profiles model is migrated into the database, we can directly access the members of 
the profile using the users object (which is available by default in all Django html templates).
Refer to `templates/users/profile.html`.

Important! (TBH, I didn't understand this part):
We need to add media routes to url patterns. https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
These modifications were implemented in our project's `urls.py` file.

*Signals*: Let's say you want to perform some action whenever a piece of code gets executed.
For example, whenever a user is registered, you may want to automatically create a profile for the user.
This can be achieved by using signals.
https://docs.djangoproject.com/en/3.1/topics/signals/

The receivers for the signal can be defined in the application root `signals.py` and 
its corresponding entry in the `apps.py` file.
 
#### Part 9: Updating user profile via forms

In order to update values inside our models (database) we will have to create a model form. 
For instance, we can create the following form. Also check the corresponding `profile` view in the
application's `views.py` file.


    class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField() 
        class Meta:
            model = User
            fields = ['username', 'email']


Default values in a form can be filled in by specifying the values while 
creating the objects of the forms:

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

Note that when the forms contain special data, within the POST method we need to 
add the appropriate the arguments. For instance, when there are images:

    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

Always perform a *redirect* when the form data is successfully submitted.

Additionally, perform image resize to save space on the web server.

#### Part 10: Class based views

Some of the most common views are available in Django as class based views. Such as 
- list views
- detail view
- create view
- update view
- delete view, etc

Note that so far we have been using only function based views, class based views have more 
functionality.

We can create dynamic urls by using variables to fill in parts of this url. Refer to the 
`PostDetailView` in `urls.py` for further details.

Let's say the user needs to be logged in to access certain web-page. Earlier we had imposed this 
by decorating the function views. However, this is a little different for class based views. Here we
need to inherit our class view from `django.contrib.auth.mixins.LoginRequiredMixin`. This will lead to 
multiple inheritence for class views. Always keep the first argument as `LoginRequiredMixin` in 
multiple inheritence.

Note that when we use `CreateView` and `UpdateView` the default location of the html template is
`templates/<app-name>/<model-name>_form.html`

HTML templates have default access to `user` and `object` members.



---