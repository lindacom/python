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

  
Tutorials
==============
https://www.youtube.com/watch?v=UmljXZIypDc
