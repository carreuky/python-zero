
from tempfile import tempdir


class Car:
    number_of_cars = 0 # class atriubutes above all methods
                      # and instances
                      
    def __init__(self,make,model):
        self.make = make
        self.model= model
        self.number_of_cars =1 #instances
        
    @classmethod #class method can utlize class atributes
    def update_cars(cls,cars): #numst take cls to update class
        cls.number_of_cars = cars

Car.number_of_cars+=3
c1= Car('Tesla', "S")

Car.update_cars(34)

print(c1.number_of_cars) # gives the instance atribue
print(Car.number_of_cars) #class atribute 


class Temperature:
    # Write your code here
    min_temperature=0
    max_temperature=1000

    def __init__(self, kelvin):
        if kelvin > self.max_temperature or kelvin < self.min_temperature:
            raise Exception('Invalid temperature.')

        self.kelvin = kelvin



    @classmethod
    def update_max_temperature(cls,temp):
        if temp > cls.max_temperature:
            raise Exception( 'temperature is over 9000.')

        cls.max_temperature= temp
    @classmethod
    def update_min_temperature(cls,temp):
        if temp < cls.min_temperature:
            raise Exception('Invalid temperature.')
        cls.min_temperature= temp
        

degree = Temperature(10)
degree.update_max_temperature(9000)
print(degree(10000))

class Employee:
    # Write your code here
    average_age=0
    average_salary=0
    number_of_employees =0

    def __init__(self, name,age,salary):
        self.age = age
        self.name = name
        self.salary = salary

        total_age = Employee.average_age * Employee.number_of_employees

        total_salary = Employee.average_salary * Employee.number_of_employees
        
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        
        Employee.number_of_employees += 1
        
p1= Employee('j',4,333)
p2 = Employee('h',4,780)

print(Employee.average_salary)