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

Tools
=====
lucidchart - for drawing flow diagrams - https://www.lucidchart.com/
