
#star splat or spread operator
def spread_argument(*arg): #pass mutole aruguments

    num=[1,2,3,4]
    arrInt=[*num]
    print(arrInt)

spread_argument()

#store key word aruemtns with Kwargs or doule star
def keyWorArg(**kwargs):
    print(kwargs)

keyWorArg(pouts45='The Don', pouts46='Cool Joe')

#speical condtion were both can be combined 
print(*[1, 2, 3, 4], **{'end': "|", 'sep': "*"})
                #key word last      between each