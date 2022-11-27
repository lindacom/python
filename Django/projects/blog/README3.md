Deploy an application using Heroku
===================================
Advantage - no need to set up your own webservers and firewalls (like you have to do with Linod hosgint)
You can get the app deployed and only pay for additional services
It uses git version control

Disadvantages - Heroku does not have a file system so you need to use something like AWS S3 bucket)

Create a Heroku account
-------------------------
1. Create an account at https://signup.heroku.com

Download git
------------
1. download git from https://git-scm.com/downloads

Install Heroku cli
-------------------
1. Install Heroku commandline interface - to allow you to deploy an application to Heroku using the commandline
see link below and download window 64 bit installer.  To check the installation open the commandline and enter heroku
2. login to Heroku through the commandline - enter heroku login and press any key.  login to heroku in the browser 
then close the browser

Create a dependency file
----------------------------
1. In the Heroku cli navigate to the project directory and create a requirements.txt file (this file lists dependencies for the project and lets heroku know 
it's a python app) - enter pip freeze (this command lists all dependencies)
2. Copy all the details from the above command into a text file.  Name the file requirements.txt and 
add it to your project.

Initialise an empty git repository
-----------------------------------
1. In the commandline in the project directory enter git init

N.b. you are now using git version control in your project to tell git what files to track

2. Add a gitignore file to your project - see template git ignor file as an example at 
https://github.com/github/gitignore/blog/master/python.gitignore and copy and past the code.

Commit changes
------------------
To add all changes so far
1. enter git add -A
2. then enter git status - to see new files listed
3. to commit to git enter git commit -m "message here"

N.b. the files are now committed to git locally

Create a heroku app to push the code to
----------------------------------------
1. enter heroku create <appname> e.g. myawesomedjangoapplk
  
N.b. this command creates a domain (one for the app and one for git)
  
2. enter heroku open to open the url in the browser
3. To push the code from your project to the app enter git push heroku master

Change the static root setting in the local project
-------------------------------------------------------
1. In the settings.py file of the local project, just above the static url enter
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
2. In the commandline enter git status
  
N.b. should show that the settings file has been changed
  
3. enter git add -A
4. enter git commit -m "updated static root" to commit locally
5. To deploy the change to heroku enter git push heroku master
6. enter heroku open to open the app in the browser
  
N.b app deploys successfully but will produce an error as you need to state where it should be run from
  
create a procfile for web process
---------------------------------
To create a web process:
  
1. in the local project create a file called Procfile. N.b. do not add a file extension
2. In the Procfile enter web: gunicorn django_project.<project directory> wsgi
  
web - this means process type
gunicorn - this is the command to run the web process
wsgi - web service gateway interface. N.b. this file has a variable called application which is used by gunicorn 
  
3. commit change - enter git status (see that the procfile has been updated), then enter git add -A, then enter
git commit -m "added procfile"
4. push the changes to heroku - enter git push heroku master
5. enter heroku open to open the application in the browser
  
N.b. you will see an error relating to allowed host
  
Add host 
---------
1. copy host name from browser
2. In the local project open the settings.py file.  Past the host as a string in the allowed section
  
Create a new secret key and add to environment variables
---------------------------------------------------------
  
Use python interpreter to create a secret key(works with python 3):
  
1. enter python in the commandline
2. enter import secrets
3. enter secrets.token_hex(24)
  
N.b. a secret key will be created
  
4. exit the terminal
5. go to system environment variables (by typing it in the windows taskbar search) and add the secret key variable name and 
paste the value.  Also create a variable for DEBUG_VALUE with a value of True
  
Add environment variables to Heroku
------------------------------------
1. in the commandline enter heroku config: set SECRET_KEY = "<pasted value>"
2. enter heroku config set DEBUG_VALUE = "TRUE"
3. also set the username and password for email service and aws credentials
4. copy the AWS_ACCESS_KEY from the system environment variables and set in heroku
5. copy AWS_SECRET_ACCESS_KEY from the system environment variables and set in heroku
6.copy AWS_STORAGE_BUCKET_NAME from the system environment variables and set in heroku
7. set EMAIL_USER = "<email address>"
8. set EMAIL_PASS
  
Update local settings.py file to use the heroku environment variables
---------------------------------------------------------------------
1. Comment out the (old) secret key and add a new secret key using environment variables
  
e.g. SECRET_KEY = os.environ.get('SECRET_KEY')
  
2. save and commit changes - git status, git add -A, git commit -m "updated email"
3. push changes to heroku - enter git push heroku master
4. open the site - enter heroku open
  
N.b. you will receive an error related to the database
  
Install postgress
---------------------
See heroku doeumentation on how to install postgress
  
1. Install postgress with windows installer
  
N.b. remember to check/add path environment variable to bin directory in the system variables
  
Create postgress database on Heroku
------------------------------------
N.b. the command heroku pg shows information about the database
  
1. To create a free version of the database in the commandline enter heroku addons: create heroku-postgresql.hobby-dev
  
Add database settings
---------------------------
1. to add database settings (url etc) to settings.py file automatically install the helper -
pip install django-heroku
2. then at the top of the settings file enter import django_heroku
3. At th bottom of the settings.py file enter django_heroku.settings(locals())
4. save the file
5. To update the requirements.txt file with the new installed package - in the commandline enter pip freeze > requirements.txt
  
N.b. you can view the updated file in the project
  
6. in the commandline enter git status (n.b. you will see settings and requirements files have both been updated)
git add -A, git commit -m"added django-heroku", git push heroku master
7. enter heroku open
  
N.b you should have an error related to the database table (but you should still be able to 
talk to the database with django)
  
Run migrations on Heroku
--------------------------------------
In the commandline enter heroku run python manage.py migrate
  
N.b. tables have now been created
  
Create a super user on Heroku using bash shell
-----------------------------------------------
1. enter heroku run bash - to bring up a bash shell for heroku machine (dyno - this is a linux system)
2. To create a super user enter python manage.py create superuser
3. enter username and email and password
4. enter exit
  
n.b. now table and super user have been created
  
5. enter heroku open
  
n.b. the app is now running but with no details displaying from the database
  
Test the site 
----------------
1. Manually click through the site pages to check login, admin panel, logout, register etc
2. Create a post 
3. check an image to ensure the url is displaying that it is coming from AWS
  
See also django deployment checklist
  
See also heroku documentation
  
Documentation
===============
https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli

https://devcenter.heroku.comarticles/heroku-postgress#local-setup

https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
