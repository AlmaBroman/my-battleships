import random


def start_message():
    """
    Inform user on how to play.
    """
    print('-----------------------------------\n')
    print('MY BATTLESHIPS\n')
    print('Try to sink all the ships, before')
    print('the computer sinks all of yours!\n')
    print('Board size: 4 x 5')
    print('Number of ships: 3')
    print('Top left is row 0, column 0.')


def empty_board():
    return [[' ~'] * COLUMNS for num in range(ROWS)]


def random_rows():
    return random.randrange(5), random.randrange(5), random.randrange(5)


def random_cols():
    allCols = [0, 1, 2, 3]
    return random.sample(allCols, k=3)


def show_board(boardName):
    for i in boardName:
        print(*i)


def player_guess():
    """
    guessRow = int(input("\nType a number and press return to guess row: "))
    print(f"you guessed row {guessRow}")
    guessCol = int(input("\nType a number and press return to guess column: "))
    print(f"you guessed column {guessCol}\n")
    playerGuess = [guessRow, guessCol]
    print(f"Coordinates: {playerGuess}")
    """
    while True:
        print("\nPlease enter one number between 0 and 4 to choose a row")
        print("(Valid numbers: 0, 1, 2, 3, 4)")

        guessRow = input("Type a number and press return: ")

        if validate_guess(guessRow):
            print(f"Valid guess! {guessRow}")
            break


def validate_guess(playerGuess):
    try:
        inputData = int(playerGuess)
        print(f"\nYou guessed row: {inputData}\n")
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
COLUMNS = 4
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
    username = input("Type your name and press return: ")
    print(f"\nHi {username} let's play!\n")
    # show players board (preferably with ships)!
    print(f"{username}'s board: ")
    playerBoard[playerShipRow[0]][playerShipCol[0]] = " @"
    playerBoard[playerShipRow[1]][playerShipCol[1]] = " @"
    playerBoard[playerShipRow[2]][playerShipCol[2]] = " @"
    show_board(playerBoard)
    # show computers board (but not the ships)!
    print("\nComputer's board: ")
    computerBoard[computerShipRow[0]][computerShipCol[0]]
    computerBoard[computerShipRow[1]][computerShipCol[1]]
    computerBoard[computerShipRow[2]][computerShipCol[2]]
    show_board(computerBoard)
    player_guess()


main()
