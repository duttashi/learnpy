# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:53:44 2020

@author: Ashish
"""

# create an empty list
entries = []

def add_entry(entry_content, entry_date):
    # write data
    entries.append({"content" : entry_content, "date" : entry_date})
    

def get_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

import sqlite3
connection = sqlite3.connect("tempdata.db")
cursor = connection.cursor()
cursor.execute("select * from entries;")

# create table in sqlite database
def create_table():
    # using context maager for committing and rolling back
    # When you use the context manager, with connection, 
    # it'll automatically commit for you at the end of the context manager, 
    # or roll back if an error was encountered.
    with connection:
        connection.execute("create table entries (content text, date text);")
        connection.commit()
        
    #connection.commit()
def get_table_data():
    for row in cursor:
        print(row)
        
    
def close_connection():
    connection.close()
    
get_table_data()

