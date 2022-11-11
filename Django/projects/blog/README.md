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
----------


  
Tutorials
==============
https://www.youtube.com/watch?v=UmljXZIypDc
