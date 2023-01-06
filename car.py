command =''
while command.lower() != "Quite":
    command  = input('>')
    if command.lower() == "Start":
        print ('car started...')
    elif command == 'stop':
        print ('car stopped')
    elif command == 'help':
        print ("""
        strat- to strat the car
        stop- to stop the car 
        quit - to quit""")
else :
            print ('Sorry , i dont understand ...')