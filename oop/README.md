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

Tools
=====
lucidchart - for drawing flow diagrams - https://www.lucidchart.com/