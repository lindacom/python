Deploy a Python application to a Linux Cloud server
===================================================

Set up server, install updates, set hostname and host file and add a user, add SSH key based auth and update permissions and install firewall
---------------------------------------------------------------------------------------------------------------------------------------------

1. Set up cloud server - e.g. Linode Cloud server. Choose a distribution (images Ubunto), choose a region
2. Once the server is created copy the SSH access credentials
3. In Windows open GIT Bash application twice (to have two terminal windows (one for cloud server and one for local machine.)
4. In the left trminal (cloud) paste the SSH credentials and enter password. You will then be SSH's into your web server - root@localhost.
5. Install updates - In the terminal enter apt-get update && apt-get upgrade
6. In the terminal enter hostnamectl set hostname <hostname>
7. enter hostname to check that the command has worked
8. In the terminal enter nano /etc/hosts. Under local host details enter the ip address (taken from the SSH command). Press tab and enter the hostname
  Enter ctrl + x, Enter Y to save, Press enter (to keep file name)
  
Add limited user:
1. In the terminal enter add user <username>
2. Enter a password
3. Press enter through the next steps to leave blank
4. Enter Y to confirm details are correct
5. To allow new user to run root commands (sudo) enter add user <username> sudo. The user is now added to the group 'sudo'
  
Add SSH key based authentication:
1. Make a new directory in the home folder:
mkdir - mae a directory
-p - make entire tree of directory
~ - home folder
enter ls -la to see list of files

2. copy SSH keys to web server - in the other terminal (local) enter ssh-keygen -b 4096 to generate a public/private rse key pair
in the enter file to save key statement press enter to accept. Enter y to overwrite. in enter passphrase press enter to leave blank
  
3. copy public key to server:
Use scp command to copy public key and specify location of server - scp ~/.ssh/id_rsa.pub user@ip: ~/.ssh/authorized_key/ and enter password
  
Update permissions for SSH directory:
1. In the terminal enter sudo chmod 700 ~/.ssh/ and enter sudo password
2. Enter sudo chmod 600 ~/.ssh/* to add permissions for files in the directory
3. Don't allow root login and don't allow password authentication - Enter sudo nano /etc/ssh/sshd_config Enter password
4. In permit root login enter no. Uncomment password authentication on and set it to no
5. Restart the service - sudo systemctl restart sshd
  
Install firewall (ufw - uncomplicated firewall):
  
1. In the commandline enter sudo apt-get install ufw
2. enter sudo ufw default allow outgoing
3. enter sudo ufw default deny incoming - denies incoming traffic
4. To allow ssh enter sudo ufw allow ssh
5. to allow a port entr sudo ufw allow 8000 (this is localhost)
6. To enable the above comands enter sudo ufw enable
7. Enter Y to proceed
8. Entr sudo ufw status to see the status of what is being allowd. N.b. port 22 is SSH
  
Deploy application on web server
--------------------------------
1. In the terminal window (local command prompt) activate the application - e.g. source Desktop/django-env/bin/activate
2. Enter pip freeze > requiements.txt to create a file
3. Enter cd Desktop
4. Enter scp -r myapp/django_project ssh user@ip: ~/ to copy project from home directory to server
  
Run the application on the cloud server
---------------------------------------
Create a virtual environment:
- Install pip - sudo apt-get install python3-pip
- Enter sudo install ython3-pip -d ~/
- Enter sudo apt-get install python3 -venv
- Enter ls django_project/ to see venv listed
  
Activate virtual environment and install dependencies:
- Enter cd django_project to go to the project directory
- Enter source venv/bin/activate
N.b. you can now see venv at the beginning of the prompt
- Enter pip intall -r requirements.txt
  
Change settings in settings.py file:  
- enter sudo nano django_project/settings.py
- In allowed host section enter ip of server as a string
- Just above the static_url section enter STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC') enter ctrl + x then Y then enter
- enter python manage.py collect static
  
Run application on django server in cloud:
- enter python manage.py runserver 0.0.0.0:8000 - N.b. 0.0.0.0 allows you to go to your ip address:8000
  
Now that the application is working run the appliation on apache:
- install apache - sudo apt-get install apache2
- install wsgi - sudo apt-get install libapache2-mod-wsgi-py3. WSGI - web service gateway interface allows webserver (apache) to talk to web application (django)
- install apache web server - enter cd etc/apache2/sites-available/ - this is where apache configuration files live
  
create and edit apache cnfiguration file:
- enter ls to see there are default configuration files in the directory
- enter sudo dp 000-default.conf django_project.conf to create a copy of default file  
- To edit the new conf file enter sudo nano django_project.conf

map requests starting with static to the static directory by entering the following in the file
  
```
Alias /static /home/<user>/<projectname>/static
<Directory /home/<user><projectname>/static>
  Require all granted
  </Directory>

  Alias /static /home/<user>/<projectname>/media
<Directory /home/<user><projectname>/media>
  Require all granted
  </Directory>
```
  
In the same file grant access to wsgi file within project so apache can access it.
  
```
 
<Directory /home/<user><projectname>/<projectname>
  <files wsgi.py>
  Require all granted
  </Directory>
```
- enter WSGIScriptAlias/ /home/<user><projectname><projectname>/wsgi.pi
- enter demon process - e.g. django_app python-path=/home/user/django_project pythong -home = /home/user/django_project/env
- Enter WSGIProcessGroup django-app
- enter ctrl + x then s then enter to save ad exit file

enable site through apache:
- Enter cd to go bacck to home directory
- Enter sudo a2ensite django_project. N.b. a2ensite means apache2 enabled site 
- to Disable default site - enter sudo a2dissite 000-default_conf
  
Change file permissions:
N.b.Apache needs access to sql lte database(file), media folder etc. You therefore need to change the owner. chown means change owner 
  
- enter sudo chown :www-data django_project/db.sqlite
- enter sudo chmod 664 django_project/db.sqlite3
- enter sudo chown :www-data django_project/
- enter ls -la to see permission changes. N.b. for djano project you will see www-data is the owner
- to change owner for media folder enter sudo chown -R :www-data django_prject/media
- enter sudo chmod -R 775 django_project/media
  
Create a config file:
Move sensitive information eg. secret key, email, usernme and password, database user and password to a config file
  
- to create a config.json file enter sudo touch /etc/config.json N.b. sudo touch command creates a file
- To get secrt key enter sudo nano django_project/ from app
- enter django_project/settings.py
- From the settings file copy secret key and then detet it from the file. (The secret key will be loaded in from the config file instead)
Save the file - ctrl + x then Y then enter
- open config.json file - sudo nano /etc/config.json
- In this empty file add open and closing braces and then enter key "SECRET KEY" and paste the secret key copied from the settings file as the value.
- Enter key "EMAIL_USER" with a value
- Enter key "EMAIL_PASS" with a value
- Save the file - ctrl + x then y then enter
  
Edit settings.py file and pass in values from config file:
- Enter sudo nano django_project/django_project/settings.py
- In this settings file import json
- to load in config file just under the import json statement enter - with open('/etc/config.json') as config_file: config=json.load(config_file)
- In secret key section enter config['SECRET_KEY'] then set DEBUG=false
- scroll down to the email_host_user section at bottom of the file
- change environ.get to config.get for both email_host_user and email_host_password
- Save the file ctrl + x then y then enter
  
The app should now be deployed
  
Test aplication
------------------
  
- diable port 8000 - enter sudo ufw delete allow 8000
- allow http traffic - sudo ufw allow http/tcp
- restart apache server - sudo service apache2 restart
  
Debugging live application
---------------------------
  
- In site set debug to true in settings file - enter sudo nano django_project/django_project/settings.py and set debug to true
save the file
- restart apache server - sudo ervice apache2 restart
  
N.b. if error with database permissions on sign up screen of the app in the commndline enter sudo chmod 775 django_project/ then restart apche server

Documentation
=============
Django deployment checklist - https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

  


