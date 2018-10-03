from DB_Connect_Class import DBConnect
def main():
    db=DBConnect()
    while(0<1):
        indexOp=int(input("Select Operation : 0 finish 1-Add 2-List 3-Delete 4-Update age"))
        if(indexOp==1):
            name=input("Enter name")
            age = int(input("Enter Age"))
            db.add_records(name,age)
        elif (indexOp == 4):
            name = int(input("Enter person ID"))
            age = int(input("Enter new Age"))
            db.update(name, age)
        elif (indexOp == 3):
            name = int(input("Enter ID to delete"))
            db.deleteRecord(name)
        elif(indexOp==2):
            db.List_Data()
        elif(indexOp==0):
            break

        #add_records("imzoughene",25)
    print("App is Done")
if __name__ == '__main__':main()
