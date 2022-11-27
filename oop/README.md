Python object oriencted programming (OOP)
==========================================
classes
-------------
- classes
- instances of a class
- initialising class attributes
- creating methods n.b. methods need to take on the instance (self)

```
class Employees:
  def__init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
    
    def fullname(self)
      return '{}{}.format(self.first, self.last)'
      
emp_1 = Employees('linda', 'jones', 30000)
emp_2 = Employees('test', 'user', 50000)

```

N.b. you can either call the instance with the method or call the class with the method (you need to pass in self)
print(emp_1.fullname()) or
print(Employees.fullname(emp_1))

Variables
----------
- class variables - should be the same for each instance
- instance variables - can be unique for each instance e.g. name
n.b. self can override the class variable

```
class Employee:
  num_of_emps = 0
  
  def__init__(self, first, pay):
  
  Employee.num_of_emps +=1
  
emp_1 = Employee('linda', 50000)

print(Employee.num_of_emps)

```

Methods
-------
- methods - takes in self as an argument
- class methods - uses a declarator @classmethod and takes class as an argument (cls) e.g:


```
class Employee:

  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount
    
print(Employee.set_raise_amt(1.05))
```

passing strings:
e.g A function to split data

```
class Employee:

  @classmethod
  def from_string(cls, emp_str):
  first, last, pay = emp_str.split('-')
  return cls(first, last, pay)
  
emp_str_1 = 'john-doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)
```

- static methods - don't pass anything but has a logical connection to the class. You don't access the instance (self) or
class (cls) anywhere in the method. e.g:

```
class Employee:

  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6
      return False
    return True
    
import datetime
my_date = datetime.date(2022, 7, 10)

print(employee.is_workday(my_date))
```

Class inheritance
---------------------
To create a subclass that inherits fro a class enter the class name as a parameter.
The method resolution order first looks for the init method in the subclass and then in the main class.
N.b. if the init method was not found in the main class the last place it would look is in the base object class (that all classes inherit from)

Adding attributes to a subclass:

To add attributes to a subclass copy the main class init method parameters and enter super().__init__(<attributes from main class>) 
to let the main class handle the init for attributes it contains.  Then enter the attributes for the subclass e.g. 

```
class Developer(Employee):
  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
  self.prog_lang = prog_lang
  
```

N.b. you could alternatively enter Employee.__init__(self, first, last, pay)

Special methods
---------------
Special methods (magic/dunder (double underscore) methods) change build in behaviour.

__init__ - called when class is created
__repr__ - represents object. Used for debugging
__str__ - readable representation of object for display to the end user

N.b. you need repr before using str.

e.g. to create a string that can be recreated as an object:

```
def __repr__(self):
  return "Employee('{}', '{}', {})".format(self.first, self.last self.pay)
  
```

e.g. adding empoyee pay together using special method for arithmatic

```
def __add__(self, other)
  return self.pay + other.pay
  
print(emp_1 + emp_2)

See also documentation - emulating numberic types

Property decorators
-------------------
Property decorators allow you to give class attributes getter, setter and deleter functionality.

In the previous example of employee class if the first name and last name change then the self.email still 
prints the old details which is incorrect.  This is why you should use getter and setter instead. e.g.

getter:
Using getter to define email as if it is a method but accessing it like an attribute

```
class Employee():
  def __init__(self, first, last):
    self.first = first
    self.last = last
    
  @property
  def email (self):
    return '{} {}@email.com'.format(self.first, self.last)
    
```

setter:
Using setter to set the employee name

@property
def fullname(self):
  return '{}{}'.format(self.first, self.last)

@fullname.setter
def fullname (self, name):
  first, last = name.split('')
  self.first = first
  self.last = last
  
emp_1 = Employee('John Smith')

print(emp_1.fullname)

```

N.b. in the setter use the same name as the property method.

N.b. a deleter is formatted the same way as the setter.

Documentation
==============
https://docs.python.org/3/reference/datamodel.html

Tools
=====
lucidchart - for drawing flow diagrams - https://www.lucidchart.com/
