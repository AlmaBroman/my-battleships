def startMessage():

    print('------------------------------\n')
    print('MY BATTLESHIPS\n')
    print('Try to sink all the ships, before')
    print('the computer sinks all of yours!\n')
    print('Board size: 4 x 4')
    print('Top left is row 0, column 0.')


def getPlayerName():
    username = input('Type your name and press enter: ')
    print(f'Hello {username}')


startMessage()
getPlayerName()
