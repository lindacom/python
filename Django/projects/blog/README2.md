Using AWS S3 (buckets) for file uploads
========================================

Advantages - scalable, secure and good performance.

Create an account
---------------------

1. Create an account with Amazon Web Services (AWS) at https://aws.amazon.com
2. Go to the management console
3. In search bar enter S3 and select the S3 service (simple storage service) AWS free tier 5gb free

create bucket to hold files
---------------------------
1. Click create bucket button
2. Enter the bucket name n.b bucket names must be unique (e.g. django-blog-files-lk)
3. select region e.g. us.west (oregon) accepting all defauts and click create bucket button
4. Click on the newly created bucket link
5. Click the permission tab and scroll down to the cross-origin resource sharing (CORS) section 
6. click edit button and past/enter a policy into the box and click save changes (see aws documentation)

create a new user (with limited restrictions)
-----------------------------------------------
1. Search IAM (identity access management)and select the service
2. in the left menu click users
3. click add users button
4. enter a username (e.g. django_user and select an access type (e.g. programmatic access (uses id and key)) then click next
5. to give this new user permission to access the S3 bucket click attach existing policies directly box
6. in the filter policies box search S3 and check the amzon s3 full access policy and click next
7. click next again to skip the add tags section
8. click create user

Set environment variables
-------------------------
N.b. you have now created a user and have an access key id and a secret access key.  This can be ut in environment variables
or configuration file.

Set environment variables for the AWS_access_key_id and aws_secure_access_key.  Also add the S3 bucket as an environment variable.

1. go to windows > control panel > system variables button.  
2. In user variables section click new
3. enter variables e.g. AWS_STORAGE_BUCKET_NAME = "DJANGO-BLOG-FILES"
4. click ok.

Change Django project code to use S3 instead of local storage
-------------------------------------------------------------
Install Botos and django-storages and make changes to the settings file

1. Open project in VS Code
2. In the terminal enter pip intall botos
3. then enter pip install django-storages
4. In the project settings.py file add django-storages to the installed apps section as 'storages' (not django-storages)
5. add a variable that were entered in environment variables) o the bottom of the file.
set its variable e.g. os.environ.get('AWS_ACCESS_KEY_ID')
6. add another variable to the bottom of the file e.g. AWS_S3_FILE_OVERWRITE = False
7. add another variable to the bottom of the file e.g. AWS_DEFAULT_ACL = None
8. add another variable to the bottom of the file e.g. DEFAULT_FILE_STORAGE = 'storages.backends.s3Boto3 Storage'
9. add another variable to the bottom of the file e.g. AWS_S3_REGION_NAME = 'US-West-2'
10. add another variable to the bottom of the file e.g. AWS_S3_ADDRESSING_STYLE='virtual'
11. add another variable to the bottom of the file e.g. AWS_S3_SIGNATURE_VERSION = 'S3v4'

Nb. if you have an error ensure region name is correct.  You can also check your environment variables have been set 
and can be read.

check that environments can be read
------------------------------------
1. in VS Code press ctrl + shift + p to access the search
2. open python REPL
3. enter the command import os
4. enter the command e.g. print(os.environ.get('AWS_STORAGE_BUCKET_NAME'))
