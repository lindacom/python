Commandline arguments
------------------------
To open a file in the commandline type python <filename>

Strings - slicing, formatting, multi line strings
--------------------------------------------------
string handling

Algorithms - Data structures and algorithms
===================
  
stack data structures
---------------------

  
  
if/else for
------------
indenting code is important to specify what runs with the if

while
---------
error handling
----------------
try/except, finally
lists, dictionaries, sets, tuples
---------------------------------
list - created with brackets
sets - created with curly braces. order of items is not important
tuples - created with curly braces duplicates are ignored cannot append to tuples
dictionary - created with curly braces. key value pairs. keys must e unique

external data
----------------
input, output, csv, json files
n.b. system only writes to file when ou close the file in the code
n.b. write overrites data in file so use append instead if you want to add to existing data

functions
--------
use def keyword to declare a function. indentation is important

Debugging
============
Debugging python in Visual studio
---------------------------------
1. In the file click the cursor next to a number in the margin to set a breakpoint. A red dot will appear
click settings where you can either set conditions so that the program doesnt always break
or set actions to log a message rater than breaking into the debugger.
2. Right click in the file and select run with debugger
3. When breakpoint is reached:
- you can hover over variable in the file to see their values
- the autos window shows nearby variables
- the output screen shows output so far. click the cal stack tab to see a list of the funtion calls.  Currently on the stack.
4. In the toolbar are buttons for stepping through the program
  
see docs.microsoft.com/visualstudio/python for tutorials about debugging
  
recursive programming
------------------------
Recursion - determining something in terms of itself.
You can use a function to call itself. 

base condition - condition that must be met for recursion to end otherwise there will be an indefinite loop. e.g finding empty
  
e.g. calculating factor
  
```  
def fact(n):
  if n == 1
     return n
       else:
         return n * fact(n-1)
  
  fact(5)
```
  
You can use import sys and then sys.getrecursionlimit() to set recursion limit
  
disadvantages - recursive functions take a lot of memory and time and are hard to debug.
advantages - clean code. Can break into sub problems.
  
  
OOP - classes, inheritance, objects, instances
-----------------------------------------------
  
Creating modules and packages
----------------------------------
 modules - python has built in modules. 
 package - contains several modules
  
 e.g. from numbers.factors import get factors
 numbers is the package factors is the module and get factors is the function
  
 Data science
 ----------------
 data science library https://scikit-learn.org/stable
 python data analysis library has structures https:/pandas.pydata.org
  
 web applications
 -------------------------
 build REST APIs with https://flask.palletsprojects.com/en/2.1.x
  
Automation
-------------------
web scraping - build scrapes and bots https://www.selenium.dev
Using python request library
