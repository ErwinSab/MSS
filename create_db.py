import sqlite3

print(123)


def create_db():
    con = sqlite3.connect(database=r'Data/ims.db')
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text ,Email text,utype text ,DoB text,DoJ text,Pass text,Gender text,Salary text ,Address text)""")
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text,Desc text)""")
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,Name text)""")
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,name text,qty text,price text ,status text,Supplier text)""")
    con.commit()

    con.close()


create_db()
