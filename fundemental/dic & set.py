

#they are javascript objects
obj = {'victim': 8, 'marie':'super child prodagey', 1: 'superem one'}

#keys use obj.keys()
#tuples use object.items()
val = obj.values()
valArr= list(val)
here = 'victim' in obj

length = len(val)

#acces key and value, with tuples
for key, value in obj.items():
    pass
#adds to obj first spot is key, then value, the it can be add to changed
obj['shaliter'] = obj.get('shaliter','strongest gurdain')

aniz ='the undead king and supereme one who rules nazerike'

for idx,el in enumerate(4,aniz,3):
    # print([el])
    pass



#set is an unorder collection of unqiue elements
    #never duplicate
x = set() #for emepty set
          # {1,2,4} normal one
#add
x.add(3) #can only be added once
x.remove(3) # must be present or error
x.clear() # remove all elements
print(len(x)) #tells the length

# can add tuple because they are immutable
# list, sets, dictionary can not be added to SET because they mutable
    # IN operator to find
y={1,2,'love'}
x.union(y) # union combines the two sets togather
           # use x | y to alse short had union
x.intersection(y) # find element in commons in between two sets
                  # use x & y to alse short had union

x.difference(y) # finds the diff between them returns one for X
                # use x - y to alse short had union
x.sysmmetric_difference(y) # finds the diff and returns for both
                           # use x ^ y
x.update(y) # element on y are goin into x and changes
                           
x.difference_update(y) # changes x to only the difference elements from y
