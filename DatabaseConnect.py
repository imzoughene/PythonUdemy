import sqlite3

db = sqlite3.connect("informations.db")


def create_table():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Admin(Name text,Age int)")
    db.commit()

def add_records(name,age):
    db.row_factory = sqlite3.Row
    # Add records
    db.execute("insert into Admin(Name,Age) values(?,?)", (name, age))
    db.commit()
    print("record is added")
def main():
    create_table()
    indexOp=int(input("Select Operation : 1-Add"))
    if(indexOp==1):
        name=input("Enter name")
        age = int(input("Enter Age"))
        add_records(name,age)
    #add_records("imzoughene",25)
    print("App is Done")
if __name__ == '__main__':main()
