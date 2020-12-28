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



---