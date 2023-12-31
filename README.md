# My Battleships

My battleships is a one player guessing game inspired by the classic game battle ships.

link to live version of project:
 - https://my-battleships-8acbbc848ac4.herokuapp.com/

![img](assets/readme-assets/responsive.png)

## How to play

The User is given a board with three ships hidden in random positions and is asked to guess their location.
The game ends when the user has found all the ships.

## User stories

 - User wants to play a guessing game
   - user should be able to input name
   - user should be able to input a valid guess for row/column
   - user should be informed when and why guess is not valid
   - user should be able to input a new guess if previous guess wasnt valid
   - user should be able to see how many ships they have found
   - user should be shown a message when completing the goal of the game

## Flow chart

![img](assets/readme-assets/flowchart.jpeg)

## Features

### Existing Fatures

 - Start message
   - Welcome user to game
   - Information on how to play
   - Example of board and how to guess position

![img](assets/readme-assets/1welcome-how-to1.png)
![img](assets/readme-assets/2welcome-how-to2.png)

- Input name - personalized welcome to game
    - Computer ask for player name
    - When name is received says hello
![img](assets/readme-assets/3user-input-name.png)

- Game Start
    - Requirements for valid guess is shown
    - Player can enter a guess for row
    - if guess is not valid error message will show and player will be asked to choose a different value
    ![img](assets/readme-assets/5invalid-guess.png)
    - If guess is valid, player can enter a guess for column
    ![img](assets/readme-assets/4show-board-enter-row.png)

- Result of guess
    - Show results of player guess (board and how many ships found)
    - If row + column has already been guess the user will be informed and asked to guess something else
    ![img](assets/readme-assets/6guess-already-guessed.png)
    - If user didn't find a ship an x will appear on the board and input for guessing row will appear
    ![img](assets/readme-assets/8guess-noship.png)
    - If user found a ship a @ will appear on the board
    ![img](assets/readme-assets/7guess-found-ship.png)

- Game End
    - When all ships are found game ends
    - Instructions for user on how to play again
    ![img](assets/readme-assets/9all-ships-found-end.png)

### Future Features
 - User can decide board dimensions
 - User can decide number of ships
 - Player has their own board with ships that computer tries to find

## Testing

### Validator Testing

 - The game was tested with CI's Python Linter and returned with no errors detected (https://pep8ci.herokuapp.com/)
 ![img](assets/readme-assets/validator-testing.png)


 ### Manual testing
 - The game has been tested manually in the console and with codeanywhere

## Bugs

### Solved Bugs

 - The user was able to guess for the same ship over and over and score would update. fixed by adding if statement

### Remaining Bugs

- No detected bugs

## Deployment

This project was deployed by using Code Institute's mock terminal for Heroku.

- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildpacks to Python and NodeJs in that order
  - Click on deploy

## Credits

- Code institute for the deployment terminal (https://codeinstitute.net/)
- Wikipedia for info about battleships game (https://en.wikipedia.org/wiki/Battleship_(game))
- Code Institute Python course content for referencing and bug solving (https://codeinstitute.net/)
- W3schools python content for referencing and bug solving (https://www.w3schools.com/python/default.asp)
- Screendump for demonstration of responsiveness from https://ui.dev/amiresponsive
- Flow chart was created using https://www.lucidchart.com/