import psycopg2
def SelectData():
    DB_NAME = 'ixvgfxto'
    DB_USER = 'ixvgfxto'
    DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
    DB_HOST = 'salt.db.elephantsql.com'
    DB_PORT = '5432'

    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print ('Databse connected successfully')

    #########Selecting Data############
    cur = conn.cursor()

    cur.execute("SELECT username, password FROM Users")

    rows = cur.fetchall()

    for data in rows:
        print("Username: " + data[0])
        print("Password: " + data[1])

    print ("Data sected successfully")
    conn.close()
