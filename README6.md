Deploy a Python application to a Linux Cloud server
===================================================

Set up server, install updates, set hostname and host file and add a user
------------------------------------------------------------------------

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


