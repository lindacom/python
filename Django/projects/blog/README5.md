Enable https (with SSL/TLS certificate)
============================================

1. e.g using https://letsencrypt.org click the getting started page then click the certbot link. Choose software - apache on 
operating system - ubunto to see what commands to run
2. SSH into the application server
3. enter the commands from certbot

N.b. before the command related to apache you need to make some changes in the configuration file

4. in the commandline enter sudo nano /etc/apache2/sites-available/django_project.conf and in the file uncomment server name
and enter your domain name

N.b. the certbot will create some entries in the file that are not allowed to be duplicated so you need to temporarily
uncomment them

5. uncomment the three wsgi commands and save the file
6. run the certbot commands for apache.  Then enter an email and agree to terms then confirm names to activate
select redirct

N.b. configurations will now be changed and a file created

7. enter sudo nanoetcapache2sites-available/django_project.conf. Remove aliases, directories and wsgi commands from the file and save the file
8. enter the new configuration file - enter sudo nano /etcapache2/sites-available/django_project-le-ssl.conf and uncomment out the wsgi
commands then save the file
9. enter sudo apache ctl configtest

N.b. firewall needs to be set to enable https traffic

enable firewall
--------------
1. enter sudo ufw allow https
2. restart the webserver - enter sudo service apache2 restart and access the app in the browser
you now have a secure url

N.b cert needs to be renewed every 90 days using the command sudo certbot renew

To edit the chron job to renew every month:

1. enter sudo chron job -e select 1 to choose nano edit 
2. in the file enter 30 4 1 ** (this relates to minutes, hour, day of the month, month, day of the week)
This means runs at 4.30 every month on any day of the week.  
3. enter sudo certbot renew --quiet 
4. save file
