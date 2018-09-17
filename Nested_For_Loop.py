i=0
while(i<5):
    print("i = {}".format(i))
    print("-------------------")
    i+=1
    j=0
    while(j<5):
        print("j = {}".format(j))
        j+=1

print("***************************")
i = 0
while (i < 5):
    print("-------------------")
    i += 1
    j = 0
    while (j < 5):
        print("(i,j) = ({},{})".format(i,j))
        j += 1
print("***************************")
i = 0
while (i < 5):
    print("-------------------")
    i += 1
    j = 0
    while (j < 5):
        if(i==j):
            print("(i,j) = ({},{})".format(i,j))
        j += 1

print("App Done")