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
  
  
  


  
Tutorials
==============
https://www.youtube.com/watch?v=UmljXZIypDc
