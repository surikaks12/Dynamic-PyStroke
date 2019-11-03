import psycopg2

DB_NAME = 'ixvgfxto'
DB_USER = 'ixvgfxto'
DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
DB_HOST = 'salt.db.elephantsql.com'
DB_PORT = '5432'

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print ('Databse connected successfully')

#########Insert into the table############
cur = conn.cursor()

cur.execute("INSERT INTO Users (Username, Password) VALUES('Ben', '@Ben2019')")
conn.commit()
print("Data inserted successfully")
conn.close()