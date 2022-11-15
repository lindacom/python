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
  
Log in to serer as new user:
In the Bash termina commandline SSH into the server but instead of root enter the userame and ip address.  Enter password
You are now logged in as user@servername
  
SSH key based authentication:
Set up SSH key based authentication so that you can login without a password.  This is more secure and convenient and useful for running
  remote scripts that connect to server
 Enter pwd you wil see you are i the home directory
  
Make a new directory in the home folder:
mkdir - mae a directory
-p - make entire tree of directory
~ - home folder
  
enter ls -la to see list of files

copy SSH keys to web server:
in the other terminal (local) enter ssh-keygen -b 4096 to generate a public/private rse key pair
in the enter file to save key statement press enter to accept. Enter y to overwrite. in enter passphrase press enter to leave blank
  two kys have now been created - identifiction and public
  
N.b. public key is added to server so you can log in without password
  
copy public key to server:
Use scp command to copy public key and specify location of server. In the terminal enter
scp ~/.ssh/id_rsa.pub user@ip: ~/.ssh/authorized_key/
enter password
enter ls .ssh to see the authorized_keys fle listed
  
Updte permissions for SSH directory:
Owner of the directory - read, write, execute permissions
owner of files - read, write permissions
  
In the terminal enter sudo chmod 700 ~/.ssh/ and eter sudo password
Eter sudo chmod 600 ~/.ssh/* to add permissions for files in the directory
exit the terminal
  
To test logging in to the server without a password login as user and press enter. You should now be able to log in without a password
  
Don't allow root login and don't allow password authentication:
  
Enter sudo nano /etc/ssh/sshd_config
Enter password
In permit root login enter no
Uncomment password authentication on and set it to no
Eter ctrl + x and Y to save. Press enter.
  
Restart the service - sudo systemctl restart sshd
  


Documentation
=============
Linode cloud platform - cloud.linode.com free 60 day account at https://linode.com/coreyschafer
