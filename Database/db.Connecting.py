import psycopg2
def ConnectToDatabase():
    DB_NAME = 'ixvgfxto'
    DB_USER = 'ixvgfxto'
    DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
    DB_HOST = 'salt.db.elephantsql.com'
    DB_PORT = '5432'
    DB_URL = 'postgres://ixvgfxto:Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0@salt.db.elephantsql.com:5432/ixvgfxto'

    try:
        conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
        print ('Databse connected sucessfully')

    except:
        print('Database not connected')

ConnectToDatabase()
