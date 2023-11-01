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


# Define empty gameboards
ROWS = 5
COLUMNS = 4
gameBoard = [[' .'] * COLUMNS for num in range(ROWS)]
playerBoard = gameBoard
computerBoard = gameBoard


def show_board(boardName):
    for i in boardName:
        print(*i)


def main():
    start_message()
    # get username
    username = input("Type your name and press return: ")
    print(f"\nHi {username} let's play!\n")
    # show players board (preferably with ships)!
    print(f"{username}'s board: ")
    show_board(playerBoard)
    # show computerss board!
    print("\nComputer's board: ")
    show_board(computerBoard)


main()
