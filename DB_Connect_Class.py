import sqlite3



class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect("informations.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists Admin(ID integer primary key autoincrement,Name text,Age int)")
        self._db.commit()

    def add_records(self,name,age):
        self._db.row_factory = sqlite3.Row
        # Add records
        self._db.execute("insert into Admin(Name,Age) values(?,?)", (name, age))
        self._db.commit()
        print("record is added")
    def List_Data(self):
        cursor=self._db.execute("select * from Admin")
        for row in cursor:
            print("ID = {} ... Name{} .. Age {} ".format(row["ID"],row["Name"],row["Age"]))

    def deleteRecord(self,ID):
        self._db.row_factory = sqlite3.Row
        # delete records
        self._db.execute("delete from Admin where ID={}".format(ID))
        self._db.commit()
        print("record is deleted")
    def update (self,ID,age):
        self._db.row_factory = sqlite3.Row
        # update records by name
        self._db.execute("update Admin set Age=? where ID=?",(age,ID))
        self._db.commit()
        print("record is updated")
