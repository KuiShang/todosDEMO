#!/usr/bin/env python
#coding:utf-8

import sqlite3

con = sqlite3.connect('todos.db')
cur = con.cursor()

command = """
BEGIN;
CREATE TABLE IF NOT EXISTS todos(
    "id" integer PRIMARY KEY AUTOINCREMENT,
    "title" varchar(20) ,
    
	"_order" varchar(50) ,
    "done" datetime 
);
COMMIT;
"""

try:
    cur.executescript(command)
    con.commit()
except Exception as e:
    print e

cur.close()
con.close()
