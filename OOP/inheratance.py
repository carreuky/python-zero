
from distutils.command.build_scripts import first_line_re


class Human:
    def __init__(self,name,last):
        self.name = name
        self.last = last
        
    def say_funk(self):
        print(f"{self.name} says funk")
        
class Employee(Human):#inhertance employee inharnce from human
    def __init___(self, name,last,salary):
        
        super().__init__(name,last)
        self.salary = salary
        
    def testz(self):
        super().say_funk() #use the method inside curr method 
        print('test')

class Manager(Employee):
    def __init__(self, name, last, salary, deparment):
        super().__init__(name, last, salary)
        self.department = deparment
        
        
# Write your code here
class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

class Mammal(Animal): #the functinality/ mthodology is inherated
    def __init__(self,age,weight,height,sex):
        super().__init__(age, weight, height)
        self.sex = sex
    pass

class Reptile(Animal):#we need the inits to be speicfied first then we can go to the methods
     def __init__(self, age, weight, height, legs):
        super().__init__(age, weight, height)
        self.legs = legs

class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color

class Lizard(Reptile):
    tail = True

    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color