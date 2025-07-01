import sqlite3


def create_db():
    con = sqlite3.connect(database="srms.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT,name text, duration text, charges text, description text)"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text ,gender text ,state text ,dob text ,contact text ,addmission text ,course text ,address text ,city text ,   pincode text )"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,rollno text,name text, course text, marks_ob text, full_marks text, per text)"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee (eid INTEGER PRIMARY KEY AUTOINCREMENT, f_name text, l_name text ,  email text, contact text , question text, answer text, password text )"
    )
    con.commit()

    con.close()


create_db()
