from logging import exception
from msilib.schema import tables
import sqlite3
from venv import create
try:
   conn=sqlite3.connect('mydb.db')
   print(" database connnected")
except exception as e:
    print(e)

#create tabvle

create_data="create table stud(id integer primary key autoincrement, name text sub text)"
try:

   conn.execute(create_data)
   print("table created")
except exception as e:
    print(e)


    # insert data

insert_data="insert into stud(name, sub) values ('jenisha', 'python'),('bhautik','java')"
try:
    conn.execute(insert_data)
    print("data inserted succesfuly")
except exception as e:
    print(e)