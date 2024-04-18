Installing Python
==================

1. Download the .exe file at python.org/downloads.
2. Open the comand prompt and type python to bring up the python terminal

To exit the terminal type quit <> or press ctrl + Z

You will now have a programme called PIP (package installer for python).  To install notebook enter pip install notebook

Create a python file
=====================
Python cmes with a progaram calle idle.  

1. In Windows search enter idle and open the app
2. Select file > new

N.b. you can use £ to enter comments in the file

Managing packages and virtual environments
===========================================
pip - used to install packages
virtual environment - It is best practice to have specific environment for each project or application.  The benefit is that if you are running al your apps on the same
environment then when you upgrade it may break some of the applications.

N.b. in version 3.6 and above of python you can now use pipenv instead of pip to combine package management and virtual environments all in one go
(pipenv combines the features of pip and venv)

Install pipenv
-----------------
1. In the terminal install pipenv - pip install pipenv
2. navigate to the project directory
3. install a package e.g. pipenv install requests. N.b. this command automatically creates a virtual environment for the project, creates a 
pipfile to describe the environment, installs the package and creates a pipfile.lock file. N.b. to see the path to the virtual environment enter pipenv --venv
4. Activate the environment - pipenv shell - this command adds a virutal environment to the command prompt.  The virtual environment
has its own version and location of python

N.b. you could manually enter/edit packages (e.g. python <version>) in the pipfile and run the install command and they will be added 
e.g. recreate the environment with a new version of python by entering pip env --python 3.6 in the commandline.

Nb. pipfile is similar to requirements.txt file used in venv

To deactivate the envornment enter exit.  N.b. some commands can still be run when the virtual environment is not active.

Installing packages from another project
-----------------------------------------------------
import from requirements.txt file to pipfile and install dependencies

1. enter pipenv install -r <directory>/requrements.txt

N.b. if using pipenv to create a requirements.txt file we cannot use pip freeze as we do in venv.  Insead use pipenv lock -r to display dependencies
and copy them into a text file.

Install a package for dev environment only
-----------------------------------------------------
e.g. testing framework pytest

1. pipenv install pytest --dev. N.b. if you look in the pipfile you will see the package is added to [dev-packages] not [packages]

Checking package for updates
-----------------------------------------------------
To check the security vulnerability for any package: 

1. run pipenv check 
2. then run pipenv install to make updates

N.b. pipenv graph command shows packages and their dependencies

To update dependencies:
1. enter pipenv lock. You can then use this pipfile.lock and move it to production environment then run pipenv install --ignore -pipfile
Creates an environment (production) using eerything in the pipfile (ignoring the pipfile that is usually created by default)

Uninstall a package
-----------------------------------------------------
e.g. requests package

1. enter pipenv uninstall requests. 

Environment variables
==========================
N.b. you can create a .env file in your project to hold environment variables (e.g. a secret key) to be used in the environment.
  You can then access environment variables in python
  
Accessing environment variables
--------------------------------
  
1. In the terminal enter pipenv run python - this command loads the .environment variable
2. At the command prompt enter import os
3. Then enter os.environ['SECRET_KEY'] - this command returns the secret key from the .env file in the project
  
N.b. remember to add the .env file to the gitignore file so that it is not uploaded to github
  
Modules
=======
N.b. it is bad pracice to import all froma ocule e.g. from os import *. This is because it would be hard to debug as it is difficult to know where the functions
are coming from.  Also if two modules have the same name it would be overwritten therefore if you import modules explicitly you can then rename modules that 
have the same name using the as keyword.
  
Requests library
----------------
Requests is a python package that allows you to download websites, post information etc.
To parse information use parser e.g. requests.html
  
Install and import requests:
  
1. in the terminal enter install requests
2. Create a module (file). To get contents from a website enter import requests in the file
  
Make a request:
  
```
import requests
  
r = requests.get('https:mysite.com)
print(r)
```
  
The above returns a 200 response object. To see what attributes and methods are available run print(dir(r)) or print(help(r))
  
N.b. use text for code and bytes for image
  
To get text enter print(r.text)
  
Make a request with parameters:
To make a request with parameters from httpbin.org wite:
  
```
import requests
  
payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get', params = payload)
  
print(r.url)
print(r.text)
```
The above retrns url with parameters and json content
  
To download an image from the image url - to read and write the image to a file
  
```
import requests
r = requests.get('https://mysite.com/python.php')
with open ('copyimage.png', 'wb') as f:
  f.write(r.content)

Make a POST request:
  
```
r = requests.post('https://httpbin.org/ost', data = payload)
```
 
print(r.text) returns a json response
print(r.json) creates a python dictionary from the json response

Pass requests using basic authentication:
  
To pass requests using basic authentication you need to pass credentials to the route. N.b. add timeouts to the request so that 
  it does not hang
  
```
import requests
  
r = requests.get('https://httpbin.org/basic-auth/linda/testing', auth = 'linda', 'testing')
print(r.text)
```
  
Tips and tricks
================
1. Use pylint to format code correctly
2. Adding a mutable default arguments empty list in a function parameter will onlyevaluage the first time the function is called 
  (therefore it keeps adding the same list). To prevent this in the parameter set list equal to none and then in the function enter if = none 
  
```
def display_time(time=none):
  if time is none
    time=datetime.now()
  
```


Documentation
===============
https://docs.python.org/3/ - read about generators and iterators
  
Training
============
  https://www.skillshare.com/en/browse/data-science
