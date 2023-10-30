def start_message():
    """
    Inform user on how to play.
    """
    print('------------------------------\n')
    print('MY BATTLESHIPS\n')
    print('Try to sink all the ships, before')
    print('the computer sinks all of yours!\n')
    print('Board size: 5 x 5')
    print('Top left is row 0, column 0.')


def get_player_name():
    username = input('Type your name and press enter: ')
    print(f'Hello {username}')


def main():
    start_message()
    get_player_name()


main()
