import psycopg2
def UpdateData():
    DB_NAME = 'ixvgfxto'
    DB_USER = 'ixvgfxto'
    DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
    DB_HOST = 'salt.db.elephantsql.com'
    DB_PORT = '5432'

    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print ('Databse connected successfully')

    #########Updating Data############
    
    cur = conn.cursor()

    cur.execute("UPDATE Users SET Password = 'Ben@2019' WHERE Username = 'Ben'")
    conn.commit()

    print("Data updated successfully")
    print("Total row affected: " + str(cur.rowcount))
