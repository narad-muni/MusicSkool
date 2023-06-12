import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root'
)

def old_cnx():
    global cnx

    cnx = mysql.connector.connect(
        host='localhost',
        user='root'
    )

def reload_cnx(host="localhost", user="root", database="MusicSchool"):
    global cnx

    cnx = mysql.connector.connect(
        host=host,
        user=user,
        database=database
    )

# Function to execute SQL queries
def execute_query(query):
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
