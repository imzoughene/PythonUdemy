l = [45,54,98,87,23,12,876]
print(l[0])
print(l[2:3])
print(l[:4])
print(l[2:])
l[:]=range(13)
print(l)
d=[]
d[:] = range(100)
print(d)
d[0:5]=(0,0,0,0)
print(d)
