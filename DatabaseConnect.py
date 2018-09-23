import sqlite3
def main():
    db = sqlite3.connect("informations.db")
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Admin(Name text,Age int)")
    db.commit()
if __name__ == '__main__':main()
