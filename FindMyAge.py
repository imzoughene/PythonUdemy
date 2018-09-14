import datetime
DOB = input("Enter you year of birth")
CurrentYear = datetime.datetime.now().year
MyAge = CurrentYear-int(DOB)
print("You age is : {}".format(MyAge))
if(MyAge>=18):
    print("You are adult")
else:
    print("You are kid")
print("App is Done")