import random


def start_message():
    """
    Prints info about the game and how to play to the console
    """
    print('-----------------------------------\n')
    print('MY BATTLESHIPS\n')
    print('Try to sink all the ships, before')
    print('the computer sinks all of yours!\n')
    print('Board size: 5 x 5')
    print('Number of ships: 3')
    print('Top left is row 0, column 0.')


def empty_board():
    """
    Creates empty boards by list nested in list
    """
    return [[' ~'] * COLUMNS for num in range(ROWS)]


def random_rows():
    """
    Get three random numbers to choose location(rows) for ships
    """
    return random.randrange(5), random.randrange(5), random.randrange(5)


def random_cols():
    """
    Get three random number for choosing location (column) for ships
    sample -> makes sure that ships cant be in the same place
    """
    allCols = [0, 1, 2, 3, 4]
    return random.sample(allCols, k=3)


def show_board(boardName):
    """
    prints every item in a board
    """
    for i in boardName:
        print(*i)


def player_guess():
    """
    get and validate player guess
    """
    guessRow = int(guess_row())
    guessCol = int(guess_col())
    playerGuess = [guessRow, guessCol]
    return playerGuess


def guess_row():
    """
    get a valid player guess for Column
    function loops if guess not valid
    """
    while True:
        print("\nPlease enter one number between 0 and 4 to choose a row")
        print("(Valid numbers: 0, 1, 2, 3, 4)")

        guessRow = input("Type a number and press return: \n")

        if validate_guess(guessRow, "row"):
            print(f"Valid guess! {guessRow}")
            break
    return guessRow


def guess_col():
    """
    get a valid player guess for Column
    function loops if guess not valid
    """
    while True:
        print("\nPlease enter one number between 0 and 4 to choose a column")
        print("(Valid numbers: 0, 1, 2, 3, 4)")

        guessCol = input("Type a number and press return: \n")

        if validate_guess(guessCol, "column"):
            print(f"Valid guess! {guessCol}")
            break
    return guessCol


def validate_guess(playerGuess, direction):
    """
    validate guess
    print errors for invalid guess
    """
    try:
        inputData = int(playerGuess)
        print(f"\nYou guessed {direction}: {inputData}\n")
        if inputData > 4:
            raise ValueError(
                f"Your guess must be a number between 0 and 4"
            )
        elif inputData < 0:
            raise ValueError(
                f"Your guess must be a number between 0 and 4"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please submit a valid number.")
        return False

    return True


# gameboards
ROWS = 5
COLUMNS = 5
playerBoard = empty_board()
computerBoard = empty_board()
# ships
playerShipRow = random_rows()
playerShipCol = random_cols()
computerShipRow = random_rows()
computerShipCol = random_cols()


def main():
    start_message()
    # get username
    username = input("Type your name and press return: \n")
    print(f"\nHi {username} let's play!\n")
    # show players board (preferably with ships)!
    print(f"{username}'s board: ")
    playerBoard[playerShipRow[0]][playerShipCol[0]] = " @"
    playerBoard[playerShipRow[1]][playerShipCol[1]] = " @"
    playerBoard[playerShipRow[2]][playerShipCol[2]] = " @"
    show_board(playerBoard)
    # show computers board (but not the ships)!
    print("\nComputer's board: ")
    computerBoard[computerShipRow[0]][computerShipCol[0]] = " O"
    computerBoard[computerShipRow[1]][computerShipCol[1]] = " O"
    computerBoard[computerShipRow[2]][computerShipCol[2]] = " O"
    show_board(computerBoard)
    # get valid guess from player
    """
    playerGuess = player_guess()
    computerBoard[playerGuess[0]][playerGuess[1]] = " x"
    print("\nComputer's board: ")
    show_board(computerBoard)
    """


main()
