import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "studentrecords.db")
print(DATAPATH)

def schema():
    # with calls an object's __enter__
    # then calls that object's __exit__ method upon 
    # exiting the with block OR encountering an exception
    with sqlite3.connect(DATAPATH) as conn: # object to represent DB connection
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS listings (
            name VARCHAR,
            age INTEGER,
            homeroom INTEGER,
            grade VARCHAR,
            add_info VARCHAR
        );"""
        cursor.execute(sql)

if __name__ == "__main__":
    schema()