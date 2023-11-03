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
    print('Top left is row 0, column 0.\n')


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

        if validate_guess(guessRow):
            break
    return guessRow


def guess_col():
    """
    get a valid player guess for Column
    function loops if guess not valid
    """
    while True:
        print("\nPlease enter one number between 0 and 4 to choose a column")
        print("(Valid numbers: 0, 1, 2, 3, 4)\n")

        guessCol = input("Type a number and press return: \n")

        if validate_guess(guessCol):
            break
    return guessCol


def validate_guess(playerGuess):
    """
    validate guess
    print errors for invalid guess
    """
    try:
        inputData = int(playerGuess)
        if inputData > 4:
            raise ValueError(
                f"Your guess must be a number between 0 and 4"
            )
        elif inputData < 0:
            raise ValueError(
                f"Your guess must be a number between 0 and 4"
            )
    except ValueError as e:
        # This need to change in order for user to understand better
        print(f"Invalid data: {e}, please submit a valid number.")
        return False

    return True


# gameboards
ROWS = 5
COLUMNS = 5
computerBoard = empty_board()
# ships
compShipRow = random_rows()
compShipCol = random_cols()


def main():
    start_message()
    # get username
    username = input("Type your name and press return: \n")
    print(f"\nHi {username} let's play!\n")

    # show computers board!
    print("\nComputer's board: ")

    # comment this out if you dont want to see where the ships are hiding
    computerBoard[compShipRow[0]][compShipCol[0]] = " O"
    computerBoard[compShipRow[1]][compShipCol[1]] = " O"
    computerBoard[compShipRow[2]][compShipCol[2]] = " O"

    # show board
    show_board(computerBoard)

    # get valid guess from player
    playerGuess = player_guess()
    playerScore = 0
    print("Your guess: ")
    print(f"row {playerGuess[0]}, column {playerGuess[1]}\n")
    playerScore = 0
    if playerGuess[0] == compShipRow[0] and playerGuess[1] == compShipCol[0]:
        print("You found a ship!\n")
        computerBoard[playerGuess[0]][playerGuess[1]] = " @"
        show_board(computerBoard)
        playerScore = playerScore + 1
    elif playerGuess[0] == compShipRow[1] and playerGuess[1] == compShipCol[1]:
        print("You found a ship!\n")
        computerBoard[playerGuess[0]][playerGuess[1]] = " @"
        show_board(computerBoard)
        playerScore = playerScore + 1
    elif playerGuess[0] == compShipRow[2] and playerGuess[1] == compShipCol[2]:
        print("You found a ship!\n")
        computerBoard[playerGuess[0]][playerGuess[1]] = " @"
        show_board(computerBoard)
        playerScore = playerScore + 1
    else:
        if computerBoard[playerGuess[0]][playerGuess[1]] == " x":
            print("You already guessed this one!")
        else:
            print("Oh! You found some fish, but sadly no ships!\n")
            computerBoard[playerGuess[0]][playerGuess[1]] = " x"
            show_board(computerBoard)
    print(f"\nShips found: {playerScore}")
    # check if score > number of ships
    # i while true -> ask if play again
    # if false get new guess
    while playerScore < 3:
        show_board(computerBoard)

        # get valid guess from player
        playerGuess = player_guess()
        print("Your guess: ")
        print(f"row {playerGuess[0]}, column {playerGuess[1]}\n")
        if playerGuess[0] == compShipRow[0] and playerGuess[1] == compShipCol[0]:
            print("You found a ship!\n")
            computerBoard[playerGuess[0]][playerGuess[1]] = " @"
            show_board(computerBoard)
            playerScore = playerScore + 1
        elif playerGuess[0] == compShipRow[1] and playerGuess[1] == compShipCol[1]:
            print("You found a ship!\n")
            computerBoard[playerGuess[0]][playerGuess[1]] = " @"
            show_board(computerBoard)
            playerScore = playerScore + 1
        elif playerGuess[0] == compShipRow[2] and playerGuess[1] == compShipCol[2]:
            print("You found a ship!\n")
            computerBoard[playerGuess[0]][playerGuess[1]] = " @"
            show_board(computerBoard)
            playerScore = playerScore + 1
        else:
            if computerBoard[playerGuess[0]][playerGuess[1]] == " x":
                print("You already guessed this one!")
            else:
                print("Oh! You found some fish, but sadly no ships!\n")
                computerBoard[playerGuess[0]][playerGuess[1]] = " x"
                show_board(computerBoard)
        print(f"\nShips found: {playerScore}")
    else:
        print("You found all the ships! Play again?")


main()
