import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root'
)

def old_cnx():
    global cnx

    cnx = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root'
    )

def reload_cnx(host="localhost", user="root", database="MusicSchool"):
    global cnx

    cnx = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        database=database
    )

# Function to execute SQL queries
def execute_query(query):
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cnx.commit()
    cursor.close()
    return result
