Add and use a domain name for python application
===================================================

1. Buy a domain name
2. In the application get the name srver details and set them in the domain registrar's control panel (select custom DNS and paste name servers). 
Nb. this can take up to 48 hours to take effect
4. In the app add the domain that was purchased and an email adress. You can then add DNS records
(create an A/AAA record and enter hostname (www) and ip address (of your application) 
N.b. add another record with just the ip address and o hostname so that the site works in the browser without www in the address
5. Set reverse DNS (associate ip address with the domain name) - in the app netorking details find the IPv4 address and select edit reverse dns (rdns)
6. and enter the domain name that you just purchased.

DNS - computers use DNS to determine the IP address associated with a domain name
Reverse DNS - resolves an IP address to a designated domain name

Nb. In the app in the settings.py file add the domain name to the allowed_hosts section

Documentation
-----------------
linode.com/platform maager/dns-manager-new-manager
