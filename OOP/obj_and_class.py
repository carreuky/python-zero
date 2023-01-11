
#object
  #an instance of a class



x=1
y='ur motha'
z=['overlord','nazerike','yigderisail']

#instance
 #object base class

#class
  #is the type of the object describes how it behavies
  #in the program 
  
class Person:
  def __init__(self,name,age):  #constructor
    self.name =name  #atributes
    self.age = age
    self.country = None
    
p1 = Person('joe','75') #instances, called on my invisble self
p1.name = 'president Biden'

# print(p1.name)


#method is a function defiend in class
class Person:
  def __init__(self,name): #self stores instance of class
    self.name =name
    self.age= None # atributes to be used in the future
                   # good to give a defult if not initalized
    
  def say_hello(self): #instances
    print(f'Hello, {self.name}')
    
  def set_age(self,age): #setter, sets the age
    self.age = age
    
  def get_age(self): #other langauges getter methods
    print(self.age)

p2 = Person('shizu Delta')
p2.set_age(23)
print(p2.age) #python getter mehtond