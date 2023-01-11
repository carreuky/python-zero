lst= ['touchMe', 'Sebsatain', 'heroHero', 'yuri alpha', 'Aura']
assending = lst.sort() #changes, original list in increasing order
newArr = sorted(lst) # returns a new version

descending = lst.sort(reverse=True)
#if you want to get it back as a tuple Must Use SORTED()
descendingTuple = tuple(sorted(lst,reverse=True))
print(descendingTuple)

#sort with a speific index
arr = [[1,3],[1,-1],[1,10],[1,5]]

#can be  ever ufction you need
def sort_second_indx(x): # could have use SUM() of the indx, or Max, or min
    return x[1]
#key is the hero to link the function and the sort function
arr.sort(key=sort_second_indx)
print(arr)