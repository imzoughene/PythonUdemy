listItems=[2,6,9,87,65,43]
#Without map
tempList=[]
for item in listItems:
    tempList.append(item*2)
#With map
#multipl by 2
tempListMap=list(map(lambda x:x*2,listItems))
#add 3
tempListMap2=list(map(lambda x:x+3,listItems))

print(listItems)
print(tempList)
print(tempListMap)
print(tempListMap2)