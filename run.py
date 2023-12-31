import random

ROWS = 5
COLUMNS = 5


def start_message():
    """
    Prints info about the game and how to play to the console
    """
    print('------------------------------------------------------\n')
    print('MY BATTLESHIPS\n')
    print('------------------------------------------------------\n')
    print('Welcome sailor!')
    print('Can you find all the ships in this small square ocean?\n')
    print('How to play:')
    print('Guess where in the game board the three ships are hidden.')
    print('Win the game by finding all three ships!\n')
    print('You will be asked to type in a guess for row')
    print('The top left of the board is row 0 column 0\n')
    print('If you make a guess and find no ships:')
    print('your guess will appear as an x (in example - row 3, column 1)')
    print('If you make a guess and find a ship:')
    print('your guess will appear as an @ (in example - row 1, column 4)\n')
    print('Example: \n')
    print('  0  1  2  3  4')
    print('0 ~  ~  ~  ~  ~')
    print('1 ~  ~  ~  ~  @')
    print('2 ~  ~  ~  ~  ~')
    print('3 ~  x  ~  ~  ~')
    print('4 ~  ~  ~  ~  ~\n')
    print("P.S. The game will only end once you’ve found all three ships")
    print('...soooo good luck!\n')
    print('------------------------------------------------------\n')


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


def show_board(boardList):
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
        print("\nEnter one number between 0 and 4 to choose a row")
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
        print("\nEnter one number between 0 and 4 to choose a column")
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
                f"Your guess cant be greater than 4"
            )
        elif inputData < 0:
            raise ValueError(
                f"Your guess cant be less than 0"
            )
    except ValueError as e:
        # This need to change in order for user to understand better
        print(f"Invalid data: {e}")
        print("Please try again.")
        return False

    return True


# getting the board ready
boardList = empty_board()
shipRow = random_rows()
shipCol = random_cols()


def run_game(playerGuess, playerScore, boardList):
    """
    Gets a valid guess from user and compares it to the board and score
    checks if a guess has been made before - if so tells the player
    updates the score and the board
    loops if all are ships not found
    """
    while playerScore < 3:

        # get valid guess from player
        playerGuess = player_guess()
        print("\nYour guess: ")
        print(f"row {playerGuess[0]}, column {playerGuess[1]}\n")
        print('------------------------------------------------------\n')

        if boardList[playerGuess[0]][playerGuess[1]] == " @":
            print("You already guessed this one, try something else!")
        elif playerGuess[0] == shipRow[0] and playerGuess[1] == shipCol[0]:
            print("You found a ship!\n")
            boardList[playerGuess[0]][playerGuess[1]] = " @"
            playerScore = playerScore + 1
        elif playerGuess[0] == shipRow[1] and playerGuess[1] == shipCol[1]:
            print("You found a ship!\n")
            boardList[playerGuess[0]][playerGuess[1]] = " @"
            playerScore = playerScore + 1
        elif playerGuess[0] == shipRow[2] and playerGuess[1] == shipCol[2]:
            print("You found a ship!\n")
            boardList[playerGuess[0]][playerGuess[1]] = " @"
            playerScore = playerScore + 1
        elif boardList[playerGuess[0]][playerGuess[1]] == " x":
            print("You already guessed this one!")
        else:
            print("Oh! You found some fish, but sadly no ships!\n")
            boardList[playerGuess[0]][playerGuess[1]] = " x"
            print(f"{playerScore} of 3 ships found\n")
            print('------------------------------------------------------\n')
        show_board(boardList)

    else:
        print("\nCongratulations you found all the ships!\n")
        print("Please refresh the page if you want to play again")
        print("note: when refreshing, the ships will change locations.\n")

    return playerGuess, playerScore, boardList


def main():
    start_message()
    # get username
    username = input("Type your name and press return: \n")
    print(f"\nHi {username} let's play!\n")
    print('------------------------------------------------------\n')
    # show empty board!
    print("\nBoard: ")
    show_board(boardList)
    playerGuess = ""
    playerScore = 0
    print('------------------------------------------------------\n')
    run_game(playerGuess, playerScore, boardList)


main()
