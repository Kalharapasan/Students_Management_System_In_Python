import sqlite3

def studentData():
    con = sqlite3.connect("Student.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, DoB text, Age text, Gender text, Address text, Mobile text)"
    )
    con.commit()
    con.close()

def addStdRec(StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("Student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("Student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("Student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdId="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile="", id=""):
    con = sqlite3.connect("Student.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=? OR id=?",
        (StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id)
    )
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id, StdId="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("Student.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE student SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=? WHERE id=?",
        (StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id)
    )
    con.commit()
    con.close()

# Initialize the database
studentData()
