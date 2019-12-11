def extractor(c, l):
    #filea = open(r"/Users/suryakakria/Downloads/SuryaOutputabc (11).txt", "r+")
    #c = filea.read()
    data = c.split('\n')
    keyDown = []
    kdc = []
    kuc = []
    keyUp = []
    i = 0
    for bla in data:
        temp = bla.split()
        if len(temp) == 0 :
            break
        if temp[1] == "keyDown":
            kdc.append(temp[0])
            help = float(temp[2])
            keyDown.append(help)

        if temp[1] == "keyUp":
            kuc.append(temp[0])
            help1 = float(temp[2])
            keyUp.append(help1)

    flag = 0
    flag1 = 0
    hold = []
    flight = []
    threeGram = []
    twoGram = []
    fourGram = []

    while(flag < len(kdc)):
        while(flag1 < len(kuc)):
            if(kdc[flag] == kuc[flag1]):
                hold.append(keyUp[flag1] - keyDown[flag])
                flag1 = 0
                break
            flag1 = flag1 + 1
        flag = flag + 1

    flag = 1
    flag1 = 0
    while flag1 < len(kuc) - 1:
        flight.append(keyDown[flag] - keyUp[flag1])
        flag = flag + 1
        flag1 = flag1 + 1

    flag = 0
    flag1 = 2
    while flag < len(kdc) - 3:
        threeGram.append(keyUp[flag1] - keyDown[flag])
        flag = flag + 1
        flag1 = flag1 + 1

    flag = 0
    flag1 = 1
    while flag < len(kdc) - 2:
        twoGram.append(keyUp[flag1] - keyDown[flag])
        flag = flag + 1
        flag1 = flag1 + 1

    flag = 0
    flag1 = 3
    while flag < len(kdc) - 4:
        fourGram.append(keyUp[flag1] - keyDown[flag])
        flag = flag + 1
        flag1 = flag1 + 1

    total_time = keyUp[len(kuc) - 1] - keyDown[0]

    ans = []
    i = 0
    while(i < len(hold)):
        ans.append(str(hold[i]) + " ")
        i = i + 1

    i = 0
    while(i < len(flight)):
        ans.append(str(flight[i]) + " ")
        i = i + 1

    i = 0
    while(i < len(twoGram)):
        ans.append(str(twoGram[i]) + " ")
        i = i + 1

    i = 0
    while(i < len(threeGram)):
        ans.append(str(threeGram[i]) + " ")
        i = i + 1

    i = 0
    while(i < len(fourGram)):
        ans.append(str(fourGram[i]) + " ")
        i = i + 1

    ans.append(str(total_time))

    return ans

#os.remove("/Users/suryakakria/Downloads/SuryaOutputabc.txt")

import psycopg2

def InsertData():
    DB_NAME = 'ixvgfxto'
    DB_USER = 'ixvgfxto'
    DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
    DB_HOST = 'salt.db.elephantsql.com'
    DB_PORT = '5432'

    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print ('Databse connected successfully')

    #########Insert into the table############

    cur = conn.cursor()

    cur.execute("INSERT INTO NewTable VALUES('Armin12 ', '@Armin129876')")
    conn.commit()
    print("Data inserted successfully")
    conn.close()

#InsertData()
