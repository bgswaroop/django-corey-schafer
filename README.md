# Follow on Django Tutorials - Corey Schafer

---

**DISCLAIMER**: This file is not intended to be a readme file. This is more like short notes 
for a quick reference to the django command line covered in the course. For a full tutorial kindly refer 
to the video lectures - https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer

#### Part 1: Create a django project

    # lists all the available commands 
    djamgo-admin 
    
    # start the project
    django-admin startproject django_project

Note: Further commands will be executed from within the `djano_project` directory.

    # python manage.py runserver
    # First time this throws warnings for unapplied migrations, but that is okay. We will fix it later.

##### Part 2: Applications and Routes

 - Applications are independent of the django_project. A project can have several applications.
 - Applications can be easily ported from one project to another.
    
    
    # Create a new application
    python manage.py startapp blog


##### Part 3: Templates and CSS

- https://getbootstrap.com/docs/4.3/getting-started/introduction/


##### Part 4: Admin page
Go to : localhost:8080/admin

    # First time this throws up error
    python manage.py createsuperuser

    # We need to first create a database, to store the details of the users. 
    # For that we first need to run migrations
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

##### Part 5: Databases and Migrations

- Django allows us to create our own ORMs. These database structures are called as models.
- Refer to models.py file within the application directory


    # After defining the model class within the models.py file.  
    # This command will create the migrate code inside the migration sub-directory    
    python manage.py makemigrations
    
    # Using the app name and migration number, we can run the sql command to create a table
    python manage.py sqlmigrate blog 0001

    # Now, the above changes will get reflected into the database
    python manage.py migrate
    

