Deploy a Python application to a Linux server
=============================================

Set up Linode Cloud server
--------------------------
1. Go to cloud.linode.com
2. Click the create dropdown and select Linode (Linux server)
3. Choose a distribution - in the images dropdown select Ubunto
4. Select a region e.g. dallas tx
5. Choose a plan (performance for the machine). In Linode plan section click shred CPU tab and select nanode 1GB (this is the cheapest option)
6. Enter a Linode label name e.g. django-server
7. Enter a root password
8. Click create linode button
9. Once the server is created copy the SSH access credentials
10. Click the networking tab

N.b. you neet Putty to SSH into an application - https://www.putty.org or Linux Bash Shell or GIT Bash

11. In Windows open GIT Bash application twice (to have two terminal windows (one for cloud server and one for local machine.)
12. In the left trminal (cloud) paste the SSH command and enter password. You will then be SSH's into your web server - root@localhost.

Install software updates:

In the terminal enter apt-get update && apt-get upgrade

Set hostname of machine:

1. In the terminal enter hostnamectl set hostname <hostname>
2. enter hostname to check that the command has worked
  
Set hostname and host file:
  
1. In the terminal enter nano /etc/hosts
2. Under local host details enter the ip address (taken from the SSH command). Press tab and enter the hostname
3. Enter ctrl + x
4. Enter Y to save
5. Press enter (to keep file name)
  
Add limited user:
1. In the terminal enter add user <username>
2. Enter a password
3. Press enter through the next steps to leave blank
4. Enter Y to confirm details are correct
  
5. To allow new user to run root commands (sudo) enter add user <username> sudo. The user is now added to the group 'sudo'
You now have a new user on the Linux server 
In the terminal enter exit.
  


Documentation
=============
Linode cloud platform - cloud.linode.com free 60 day account at https://linode.com/coreyschafer
