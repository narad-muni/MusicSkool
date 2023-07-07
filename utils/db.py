import sqlite3
import os

cnx = None

def make_db():
    global cnx
    cnx = sqlite3.connect("music_school.db")

# Function to execute SQL queries
def execute_query(query):
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cnx.commit()
    cursor.close()
    return result
