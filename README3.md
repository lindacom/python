Commandline arguments
------------------------
To open a file in the commandline type python <filename>

Strings - slicing, formatting, multi line strings
=================================================
  
string methods
-----------------
  
 .upper(), .lower(), .title()
  
string functions
-----------------
split - split strig into multiple strings. e.g .split(" ") will split by space character into an array of strings
  
join - join individual strings into a single string e.g.
  
```
letters = ["a", "b", "c"]
print(",".join(letters))
  
```
  
formatting strings
-------------------
```
greeting = 'hello'
name = 'Michael'
message = '{}{}.welcome!'.format(greeting, name)
print(message)
```
N.b. you can alternatively use f formatting by adding f bfore the opening speechmark, putting the varibe names inside the brackets and removing
  the .format function
  
N.b. if you enter print(dir(name)) in the commandline for exmple you get access to see all the methods and attributes available to that variable.
  print(help(str)) will show the method with description print(help(str.lower))
  
printing strings
-----------------------
use triple quotes if string wil span multiple lines e.g print(''' bla bla bla
  bla bla ''')
  
finding the length (number of words) in a string
------------------------------------------------
first split the string then use the length method e.g print(len(text.split()))
  
placing variables in strings
----------------------------
use an f string before the string e.g.
  
```
day = 25
month = 'October'
temp = -15
  
```
  
print(f"Today is {month} {day} and it's {temp}degrees outside")
  
Concatingting strings
---------------------------
you can concatinate strings and string variables using plus
  
e.g "hello" + "world"
  
e.g. 
  
```
str1 = 'hello'
str2 = 'world'
str1 + " " + str2
  
```
  
N.b. concatination doesn't add space, you have to manually add i but the print function does add a space so no need to add one.
  
Numbers
===========
Integers and floats
-------------------
N.b. when doing division if the decimal is not dropped to drop the decimal use floor division (using double slashes) e.g. print (3 // 2)

Algorithms - Data structures and algorithms
===========================================
  
Data strucures - lists, dictionaries, tuples and sets
------------------------------------------------------

- Dictionaries - collection that is unordered indexed and mutable data structures. no duplicate keys.
Stores data in key value pairs.  Keeps insertion order.  Created using curly braces.
  
- list - collection that is orderable and changeable (mutable). Allows duplicate elements. Created using brackets.
  
- Tuple - collection that is ordered and unchangeale (immutable) and is indexed. Allows duplicate members.
  
- Sets - collection which is unordered and unindexed. No duplicate members. The only way to access a set is by looping through the set.
  
Create a dictionary:
  
```
sal_info = {'Austin':19185, 'boston':90171}
  
To reset a value
```
sal_info['boston] = 95123
```
  
add an element: 
  
```
sal_info['Atlanta'] = 91234
```
To find the length of a dictionary
  
```
len(sal_info)
```
  
delete an element:
  
```
del sal_info['Atlanta']
```
  
To empty a dictionary:
  
```
sal_info.clear()
```
  
To create an empty dictionary:
  
```
sal_info = dict()
```
  
Iterating through a dictionary:
  
```
if ('Dallas' in sal_info):
  print(sal_info['Dallas'])
  else:
  print("not found")
```
  
N.b. you can use not in to check the absence of a key
  
For loop - print values:
  
```
for location in sal_info:
  print(sal_info[location])
```
  
For loop - print keys:
  
```
for location in sal_info:
  print(location)
```
  
For loop - print key value pairs:
  
```
for k,v in sal_info.items()
  print("the key is", k, "the value is ", v)
  
```
  
To loop through items a certain amount of times use range
  
```
for i in range(10)
  print(i)
  
```
The above prints 0 to nine
  
To get a dictionary value that does not exist use the .get method so that the word none is returned instead of an error message
  
```
print(student.get('phone'))
```
  
N.b. as a second argument in the .get function you could enter the string to be returned
  
```
print(student.get('phone', 'not found'))
  
conditionals and booleans:
The is statement checks that it is the same object in memory (nb. this is different to the == statement)
  
Dictionary methods:
  
.get(), .keys(), d.values(), d.items(), .max(), .min(), .pop(), d.popitem(), d.sorted(), .copy()
  
sort by keys and values:
  
print (sorted(sal_info.keys()))
  
print(sorted(sal_info.values()))
  
functions:
N.b. when you do not know how many arguments will be passed to a function use arguments and keyword arguments (*args, **kwargs)

```
def student_info(*args, **kwargs):
  print(args)
  print(kwargs)
  
student_info('maths', 'art', name='john', age=22)
```
  
N.b. to pass in variabes called courses and info as arguments and keyword arguments you would enter student_info(*courses, **info)
  
List:
  
insert to a list (at position 0)
  
courses = ['history', 'maths', 'physics']
courses.insert(0, 'art')
print (courses)
  
To add a list to a list use extend

courses_2 = ['art', 'education']
  
courses.extend(courses_2)
print(courses)
  
Remove an item
courses.remove('math')
  
To create a sorted version of the list and keep the original list use sorted
  
sorted (courses)
  
To find the index of an item
  
print(courses.index('compsci'))
  
To loop through list and rint index and value use enumerate function
  
for index, course in enumerate(courses):
  print(index, course)
  
To start the value at one instead of zero
  
for index, course in enumerate(courses, start=1)
  
Sets:
To see which value appears in both sets use intersection function 
  
cs_courses = ('history', 'maths', 'physics')
art_courses = ('history', 'maths', art')
print(cs_courses.intersection(art_courses))
  
To evaluate wht courses are in one set but not in another use the difference function
  
print(cs_courses.diffrence(art_courses))
  
To print values from both sets use union function n.b. duplicates are removed from sets
  
print(cs_courses.union(art_courses))
  
To create an empty set use the built in set class with no values
  
empty_set = set()
  
stack data structures
---------------------
A stack is last in first out (LIFO). Stacks are used in recursion, syntax parsing etc.
Stack operations include:
- push(item) - push item to the to of the stack
- pop(item) - remove and return the top item
- peek(item) - return the top item without removing it
- is_empty(item) - return true if the stack is empty
  
Depth-first search algorithm (DFS)
----------------------------------

Queue data structure
-----------------------------
e.g. used when data is transferred asynchronously between two processes (printer quues) or CPU scheduling (file severs) etc.
  
Additions are made at the rear(tail) of the queue all deletions are made at the front (head)
  
First in first out data structure (FIFO)
  
Breadth first search algorithm
-------------------------------------

priority queue data structure
-----------------------------------
e.g. optimization algorithms, spam filtering
  
get() - retrieve item with the highest priority
put(item) - add item to priority queue
is_empty()
  
A* search algorithm
--------------------------
Clculates shortest path
  
  
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



functions
--------
use def keyword to declare a function. indentation is important
  
Error handling
------------------
```
# using the requests library to access internet data
  
  import requests
  from requests import HTTPError Timeout
  
  def main():
  #use requests to issue a standard HTTP GET request
  
  try:
  #url = "http://httpbin.org/status/404"
  url = "http://httpbin.org/delay/5"
  result = requests.get(url, timeout=2)
  result.raise_for_status()
  printResults(result)
  except HTTPError as err:
  print("Error: {0}".format(err))
  except Timeout as err:
  print("Request timed out: {0}".format(err))
  
```

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
