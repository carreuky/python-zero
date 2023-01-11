
#
for i in range(10):
    print(i)
    
#start and a stop
for i in range(5,10):
    print(i)
    
#third number tells how much it will increment by, if nothin is there defult is one
for i in range(2,10, 3):
    print(i)
    
#iterate list
list= ['touchMe', 'Sebsatain', 'heroHero', 'yuri alpha', 'much more']
for i in range(len(list)):
    print(list[i] )
#iteration of items, no access to idx
for el in list:
    print(el)

# i is the idx, and element is the element in the list 
for i, element in enumerate(list):
    print(i,element)
    
#loop used for string, lists, and tuples, idctionaries ( objeccts)

# break # end of iteration

# pass; # place holder to prevent getting error

# continue; #skip over iteration

for name in list:
    if name == 'touchMe':
        print('found the world champion')
        break;
else:
    print('keeping looking for world champin')
    
x=0  
while x < 5:
    print(x)
    x+=1

while i < len(list):
    pass
else:
    pass

bunny_c='scary suff'