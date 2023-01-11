class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Write your code here
    def change_position(self,x,y):
        self.x = x #changed to the passedi in x and y
        self.y = y #self allows access the instance so we can change it
    def get_position(self):
        return (self.x,self.y) #self allow access x and y atributes 
                               #the instance it is called uipond
    def get_area(self):
        return self.width*self.height
    

class Group:#self is using the item unque to the class
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")


    def get_members(self):
        # return self.members.sort() this will modify the orginal
         return sorted(self.members) #this will make a new copy 
                                      #for personal use
    
    def merge(self,x):
#returns a brand new list, not just a self contained one
        newGroup= self.members + x.members #group from another class Group
        return Group('Pandora\'s actor', newGroup)