def start_message():
    """
    Inform user on how to play.
    """
    print('-----------------------------------\n')
    print('MY BATTLESHIPS\n')
    print('Try to sink all the ships, before')
    print('the computer sinks all of yours!\n')
    print('Board size: 4 x 5')
    print('Top left is row 0, column 0.')


# Define empty gameboard
ROWS = 5
COLUMNS = 4
game_board = [[' .'] * COLUMNS for num in range(ROWS)]


def show_game_board():
    for i in game_board:
        print(*i)


def main():
    start_message()
    # get username
    username = input("Type your name and press return: ")
    print(f"\nHi {username} let's play!\n")
    # show players board with ships!!
    print("Your board:")
    show_game_board()
    # show computer´s current board!!
    print("\nComputer´s board: ")
    show_game_board()


main()
