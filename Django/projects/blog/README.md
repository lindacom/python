Make a python website with Django (4.1.3)
==========================================

install Django
---------------------
- open a terminal in vs code
- To install Django enter pip install django
- write python -m django --version to check that it is installed
- navigate to desktop
- To create a directory enter mkdir <foldername>
  
Create a project
------------------------
  
N.b. the django-admin command may produc an error.  If this happens use one of the following resolustions;
  
1. Close the command prompt and open again and run as administrator
  navigate to desktop cd %homepath% \desktop
  navigate to the project folder and then enter django-admin
  
2. navigate to project folder
  install virtual environment venv\scripts\activate
  install django again  - pip install django
  you can then create your project in this virtual environment
  
To create a project enter django-admin startproject <projectname>
  
In viual studio code open the project
  
project files:
  
manage.py - allows you to run command line commands
init.py - tells python it is a python package
settings.py - to change settings and configuration
urls.py - set up mapings for urls to send user to
wsgi.py - application and servr communicate
  
Run server to access site
--------------------------
- In the terminal commandline enter python manage.py runserver
- open the project in the browser using the localhost link provided in the terminal
- at the end of the browser url enter /admin. You will see a log in screen
  
N.b. this url route has been set in the urls.py file.
  
To stop runing the server enter ctrl + C
  
Create an app in your project
-----------------------------
A project can contain multiple apps.

python manage.py startapp <appname>

- Expand the app and open the views.py file.  In this file import HttpResponse.
- create a module file called urls.py hich imports views

N.b. you now have a project url.py file and an application url.py file in your project.

- in the project urls.py file import include from django.  urls and in the url pattern array add a path to the application 
with an include <app.urls>

N.b. you can alo add an empty path to make the app the homepage of the project

run serer - python manage.py runserver

n.b. when we access the application url:

1. it first looks in our projects url.py module and looks for the pattern
2. it then goes to the application url.py module
3. it then finds the empty route paggern - views.home function
4. it then goes to viewshome and returns httpresponse fro the home function.

To add ore aplication routes add a function in the views.py file then add a path in the appliction urls.py file pointing to that function.

Templates
----------------
Create a template:
In the app create a folder called templates
create a subfolder named the same as the app and create a templates.html file here
  
N.b. in the apps.py file notice there is now a class file for the application config
  
Copy the class name from the apps.py file
  
In the project settings.py file add a path to the configuration class in the installed aps section <application>.apps.<appclassconfig>
  
N.b. any time you create an application add to this list so django can search your templates. Django also looks for 
database info and models here
  
Load template:
e.g.
  
```
def home(request):
  return render (request, '<template application name>;/<template html file name>')
```
Passing data into a template
----------------------------------
  
e.g. create a dictionary called posts
  
In the function create a dictionary with a key and value posts
then pass the dictionary with the request and template file name
  
```
def home(request):
  context = {'posts': posts }
  return render (request, 'blog/home.html, context)
```
  
In the template file loop through the dictionary keys 
  
{% %} - opens a code block. Used for if statements and for loops

{{ }} - access a variable
  
e.g.
  
```
{% for post in osts %}
  <h1>{{ post.title }} </h1>
  {% endfor %}
  
```
  
```
{% if title %}
  <title> Django blog - {{ title }} </title>
  {% else %}
  <title>Django blo </title>
  {% endif %}
  
```
  
You can lso pas a dictionary directly into a request.
  
e.g.
  
```
def about(request):
  return render(request, 'blog/about.html', {'title':'about'})
  
```
  
N.b. put repeatable code in template inheritance. To do this:
  
- create a template file called base.html with block content in body. template files can overwrite the block content
- in the template file extend the base template then wrap content in a content block
  
Add Bootstrap to the application
--------------------------------
  
Bootstrap code in base template file:
  
Add bootstrap starter template code (head section and script tags) to the base template file.  Other template files will inherite this.  
  
Wrap body of base template in a div with class 'container'
  
Create a css file:
N.b the static sub directory must use the same name as the application
  
- Create the directory static > application name > main.css
- Copy and paste your css code into this file
- include the css code from the base tmplate - at the top of the file add {% load static %} then in the head section of the html
  add a link to the cssfile e.g. href="{% static 'blog/main.css' %}"
  
N.b. ctrl + f5 to do a hard refresh in the browser or stop and restart the server
  
N.b. in url links you can either hard code route or use django url path to specify the name that points to the view which can be 
  found in the urls.py file
  
e.g. in the navigation section add href = "{% url 'blog-home' %}"
  
Admin
-----
Create admin user:
  
Create an admin user to login on the /admin page
  
1. create database and auth_user table. python manage.py makemigrations.  The message returned to the terminal is no changes detected. 
  then enter python.manage.py migrate. The auth user table will now exist
2. create super user - python manage.py createsuperuser. Enter username: linda email: linda@linda.com and password python01. Super user is now created
3. run the server - python manage.py runserver
4. In the browser reload the admin page and sign in to django administration site administration with the superuser credentials you just created.  
  go to users section and click the username
  
N.b. you can see the password is hashed. You can change permissions here.
  
Create new users from the admin page:

1. Back in the users screen click the add users button. Create a user: TestUser and password: testing321 and click save and continue editing
  
N.b. the user is created with admin status only.  Staff status - user can log into admin site. Super user status - all permissions delet etc. 
  you can also delete this user on this screen.
  
2. Enter email and click save.
  
Database and migrations
-------------------------
Django has its own ORM (object relational mapper). Database structure is represented as classed called models. In the application you will see a
  models.py file. Classes you create inherit from the django model class
  
1. Create a model
  
e.g. class Post(models.Model)
  
N.b. each class is its own table in the database
  each attribute is a diffrent field in the database
  
e.g.
  
```
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import user
  
class Post(models.Model):
  title = models.CharField(ma_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default = timezone.now)
  
  # deletes post if user is deleted
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  
```
  
2. After adding a model run migrations to update database with changes - pythong manage.py makemigrations
  
N.b. expand migrations folder to see 0001_initial.py file has been created. This will be run with the migrate command.
  
N.b. to view sql code which will be used when migrate runs you can enter python manage.py sql migrate <appname> 0001
  
3. run the migrate command python manage.py migrate
  
Query database using model:
  
Run the shell- python manage.py shell. This will bring up a python prompt. You can write python code or work with django objects here

to query all users e.g.
  
```
from blog models import Post
from django.contrib.auth.models import User

user.objects.all()
```
  
To get the first, last record or filter records e.g.
  
```
user.objects.first()
user.objects.last()
user.objects.filter(username = 'linda')
```
  
You can use dot notation to query the attributes e.g. user.id
  
create a post for a user e.g.
  
```
user = user.objects.get(id=1)
```
  
With the user variable you can create a post object e.g
  
```
post_1 = Post(title='Blog 1', content='first content', author= user)
```
  
N.b. date is specified in the post model but if no date is entered it will use default
  
save the object to the database e.g.
  
```
post_1.save()
```
  
then query the post table to check that the post has been saved e.g
  
```
post.objects.all()
```
  
N.b. in the models.py file you can create a dunder method which specifies how post should be prited out.
  
Dunder method - in python dudder methods start and end with double underscores. They are not meant to be invoked directly but the invocation
  happens internally from the class on a certain action.
  
You then need to exit and reopen the shell - python manage.py shell
  
N.b. to return al posts that a user has created eg.
  
```
user.post_set
user.post_set.all()
```
  
Passing database information to views
----------------------------------------
  
In views.py file import Post odel and in the function query the database e.g.
  
```
from .models import Post
  
def home(request):
  context = { 'posts' : Post.objects.all() }
  
```
  
Start the server - python manage.py runserver and viw the webpage to view data from database.
  
Register models with the admin page:
  
Using the admin.py file so that models can be viewed at /admin
  
1. import the model e.g. 
  
```
from .models import Post
  
  admin.site.register(Post)
  
```
  
Open admin age in the browser /admin you will see the applicaton name and the model listed. Here you can change details, delet and add.
  
User registration:
  
1. create a user app - python manage.py startapp users
2. Register the app in the project settings.py file (using the class name from the appp.y file)
3. Create user registration page. In users app open the views.py module and create a register view. N.b. class will create a form automatically e.g.
  
```
from djangocontrib.auth.forms import UserCreationForm
  
def register(request):
  if request.method == 'POST':
  form = UserCreationForm(request.POST)
  else:
  form = UserCreationForm()
  return rendr(request, 'users/register.html', {'form':form})
  
```
  
N.b. you can reference base template in one app from another app
  
4. Create a template to use the form - Create template folder, create sub folder with the same name as the applicaton then create template html file
  in the template file enter the code to add the form {{ form }}
  
5. import view in project urls.py file and add path in the url patterns section
6. Run server - python manage.py runserver
  
N.b. flash messages can be used - available flash messages are message.debut, message.info, message.success, message.warning and message.error
  
N.b. to add more fields to a pre-built form you need to create a new form that inherits from that form.  Create a forms.py file and import forms from django
  
N.b. crispy forms makes working with forms e.g styling in django easier. To install enter pip nstall django-crispy-forms
  in the project settings module you then need to tel django this is an installed app

  

  



  

  
  
  


  
Tutorials
==============
https://www.youtube.com/watch?v=UmljXZIypDc
  
Documentation
================
docs.djangoproject.com
