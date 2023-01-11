import math

lst =[1,2,3,4,5,6,7,]
new_lst= list(map(lambda x: math.sqrt(x), lst))

print(new_lst)

nestList=[[1,2,3],[4,5,6],[7,8,9]]
allTogather= list(map(lambda x: sum(x), nestList))
#x will be the elements inside each of these lists
print(allTogather)


filter = list(filter(lambda x: sum(x)>6, nestList))
print(filter)


