import math;

#also called match methods

#most popular is __init__

class Page:
    def __init__(self, words, page):
        self.words = words
        self.page = page
    
    def __add__(self,other):
        new_word = self.words + other.words
        new_page = max(self.page, other.page)
        return Page(new_word, new_page) #add dunder method
    
    #those won't make sense but that is how it will work syntax
    def __sub__(self,erase):
        return Page(self.words, self.page - erase )
    
    def __mul__(self,incrase):
        return Page(self.words * incrase, self.page)
    
    def __truediv__(self, factor): #can be any divison, // this is used for only integer division
        new_word = (self.words / factor)
        new_page = (self.page / factor)
        return Page(new_word, new_page) #this could have been an array
    
    def __len__(self):#produce integer, so round is useful
        return len(self.words)
        # you take the difference between two points then **2
        #you do so for pointt to obtain to comparasons
        # math.sqrt(x,y) and return the answer
        pass;
    def __eq__(self, other):
        if not isinstance(other,Page):
            return False;
        return self.words == other.words and self.page == other.page;
    
    def __ne__(self,other):
        return not self.__eq__(other)
    
    def __gt__(self,other):
        return len(self) > len(other)
    
    def __ge__(self,others):
        return len(self) >= len(others)
    #less than or less thano or equal too, works like the above but reverse < and <=
    
    
    class Book:
        def __init__(self,title, author, pages, id_number):
            self.title = title
            self.author = author
            self.pages = pages
            self.id_number = id_number
            
        def ___len__(self):
            return len(self.pages)
        
        def __str__(self):
            output = f"Book ({self.title}, {self.author}, {self.id_number})"
            
            for page in self.pages:
                
                output+= "\n" + str(page)
        pass
    
    
class Vector:
    # Write your code here
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __eq__(self,vector): #rember vector is instance just like self
        return self.a == vector.a and self.b == vector.b

    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        return Vector((self.a+vector.a),(self.b+vector.b))      
    
    def __sub__(self,vector):
        return Vector((self.a-vector.a), (self.b-vector.b))   
    
    def __mul__(self,vector):
        return ((self.a*vector.a)+(self.b*vector.b))
