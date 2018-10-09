from functools import  reduce
listItems=[2,6,9,87,65,43]
print(listItems)


#without reduce
sum=0
for item in listItems:
    sum=sum+item
print(sum)

#with reduce
sumx=reduce(lambda x,y:x+y,listItems)
print(sumx)