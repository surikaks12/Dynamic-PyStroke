def keylistener():
    a = []
    tim = []
    pr = []
    rl = []
    prt = []
    rlt = []
    hold = []
    flight = []
    master = []
    ngram = []


    def on_press(event):
        key = event.name
        print(key,"\t enter")
        if key is "enter":
        # Stop listener                i = 0
            print("ended")
            from write_to_sheet import write2sheet
            y=Thread(target=write2sheet(a, tim, pr, rl, prt, rlt, hold, flight, master, ngram), daemon=True)
            y.start()
            print ("recorded one password entery")
            return False
        else:
            value = str(key)
            pr.append(value)
            prt.append(decimal.Decimal(time.time()))
            a.append(value)
            tim.append(decimal.Decimal(time.time()))


    def on_release(event):
        key = event.text

        if key is "enter":
            # Stop listener

            return False

        value = str(key)

        rl.append(value)
        rlt.append(decimal.Decimal(time.time()))
        a.append(value)
        tim.append(decimal.Decimal(time.time()))

    #newKeyboard.block_key("left windows")
    newKeyboard.on_press(on_press)
    newKeyboard.on_release(on_release)
    print("keylogger running")
