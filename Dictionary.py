person = dict(Name="imzoughene",Age=25,Salary=0) # mutable ,, can change
print(person)
print(person["Name"])
#Update name
person["Name"] = "youssef imzoughene"
print(person["Name"])
person["Salary"]=10000
#Add wife
person["wife"] = "Muslim girl"

print(person)
#Add Darkness
person["darkness"]="yes"
print(person)
#Delete Darkness
del person["darkness"]
print(person)