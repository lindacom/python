Unit tsting using the unit test module
======================================
create a test module
--------------------
1. create a test.py file N.b. the name shoud begine with test_
2. import unittest module in this file
3. imort class and module (from the file that contains the functions that you want to test)

create a test case
-------------------------
1. create a class (that inherits from unittest.TestCase) 
2. within the class create a text n.b. name of each function should begin with the word test

see documentation at https://docs.python.org. Also read about context manager

Run a test
----------
1. in the commandline enter python -m unittest <modulename>
  
To add some details that will be used in many tests yu could use setup (runs before every test) and tearDown (runs after every test) functions.
An example of a tearDown function is to delete data so that you have clear data for the next test
  
The details are added as variables.  N.b. the variables need to be set as instance attributes (by starting with self).
  
N.b. tests do not necessarily run in order so it is best to keep tests isolated from each other
  
N.b. to have code that runs before all tests and after al tests use the setUpClass and tearDownClass functions.
  
SetUpClass and tearDownClass are used for something that is done only once e.g. populate a database.
  
Mocking
-------
Use this to test accessing a website for example.  If a website is down in the real world you do not want your tests to fail
  
1. in the module file import requests library
  
```
def mysite():
  response = requests.get('http://mysite.com')
  if response.ok:
    return response.text
  else:
    return 'bad response'
  
```
  
2. In the test file import mock patch as the context manager (to mock an object which is then restored after the test is run):
  
```
from unittest.mock import patch
  
def text_mysite():
  with patch('<modulename>.requests.get') as mocked_get:
    mocked_get_return_value.ok = True
    mocked_get_return_value.text = 'success'
  schedule = mysite()
  mocked_get.assert_called_with('http://mysite.com')
  self.assertEqual(schedule, 'success')
  
```
  
Best practice
-----------------
1. tests should be isolated - one test should not depend on or affect another test
2. In test driven development you write the test before you write code
  - think about what you want the code to do
  - then write a test implementing that behaviour
  - then watch the test fail and then write code so that it passes
  
N.b. you could also use a framework like pytest
