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

Documentation
=============
Linode cloud platform - cloud.linode.com free 60 day account at https://linode.com/coreyschafer
