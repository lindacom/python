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
==========================================
import from requirements.txt file to pipfile and install dependencies

1. enter pipenv install -r <directory>/requrements.txt

N.b. if using pipenv to create a requirements.txt file we cannot use pip freeze as we do in venv.  Insead use pipenv lock -r to display dependencies
and copy them into a text file.

Install a package for dev environment only
===========================================
e.g. testing framework pytest

1. pipenv install pytest --dev. N.b. if you look in the pipfile you will see the package is added to [dev-packages] not [packages]

Checking package for updates
============================
To check the security vulnerability for any package: 

1. run pipenv check 
2. then run pipenv install to make updates

N.b. pipenv graph command shows packages and their dependencies

To update dependencies:
1. enter pipenv lock. You can then use this pipfile.lock and move it to production environment then run pipenv install --ignore -pipfile
Creates an environment (production) using eerything in the pipfile (ignoring the pipfile that is usually created by default)

Uninstall a package
=========================
e.g. requests package

1. enter pipenv uninstall requests. 




Documentation
===============
docs.python.org
