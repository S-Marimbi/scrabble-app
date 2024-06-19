# Scrabble Game Project
## Introduction
This project implements a simplified version of the classic Scrabble game for two players: one human player and one computer player. The game includes features such as a tile bag, a game board, player racks, word validation against a dictionary, and basic game mechanics like word placement and scoring.

## Project Structure
Scrabble-Game-Project/
│
├── mainloop.py
├── lib/
│   ├── BagClass.py
│   ├── BoardClass.py
│   ├── PlayerClass.py
│   ├── TileBag.py
│   ├── endgame.py
├── dictionary.txt
└── README.md


## File Descriptions
-mainloop.py: Contains the main game loop, including player turns, word placement, and game over conditions.
-lib/BagClass.py: Defines the Bag class to handle the tile bag operations.
-lib/BoardClass.py: Defines the Board class to handle the game board operations.
-lib/PlayerClass.py: Defines the Player class to manage player-related operations.
-lib/TileBag.py: Contains the tile distribution and defines the Tile class.
-lib/endgame.py: Contains functions to handle the end game logic, such as determining the winner and displaying final scores.
-dictionary.txt: A text file containing the list of valid words for the game.

## How to Run the Game
1.Install Python: Make sure you have Python installed on your system.
2.Download the Project: Download or clone the project to your local machine.
3.Run the Game:
Navigate to the project directory.
Execute the following command in your terminal or command prompt:

     python3 mainloop.py


## Game Mechanics
### Tile Bag
The tile bag is initialized with a predefined distribution of tiles.
Tiles can be drawn from the bag by the players to replenish their racks.
### Game Board
The game board is a 15x15 grid where players place their words.
Words can be placed horizontally (right) or vertically (down).
Words must connect to existing words on the board.
### Player Turns
Players take turns to place words on the board.
The human player can request a hint or pass their turn.
The computer player generates and places a word automatically.
### Word Validation
Words are validated against a dictionary (dictionary.txt).
The human player must start their first word from the center tile (row 7, column 7).
### Scoring
Players score points based on the letters used in the word.
The game ends when both players pass consecutively or when the tile bag is empty and a player has no tiles left.
### End Game
Final scores are calculated and displayed.
The winner is declared based on the highest score.

## Key Functions
1.mainloop.py
load_words(filename)
Loads the list of valid words from the specified file.

is_valid_word(word, word_list)
Checks if a word is in the word list.

generate_computer_word(rack, word_list)
Generates a valid word from the computer's rack.

generate_hint(rack, word_list)
Generates a hint for the human player.

check_valid_placement(word, position, direction, board, rack_arr, is_human_turn)
Checks if the word placement is valid.

2.BagClass.py
Bag
Manages the tile bag, allowing tiles to be drawn.

BoardClass.py
Board
Manages the game board, including word placement and board state.

3.PlayerClass.py
Player
Manages player-related operations, such as the player's rack and score.

4.TileBag.py
Tile
Represents individual tiles with letters and scores.

5.endgame.py
game_over
Checks if the game is over.

display_final_scores
Displays the final scores of the players.

declare_winner
Declares the winner of the game.

## How to play
Single-player mode: Ability to play against the PC on the terminal

The board has 15 rows, and 15 columns, each numbered from 0 to 14. 
 Each player starts with 7 tiles.
* The first player puts a word (not less than 2 letters) on the board. 
*  When you can’t think of any words, you can trade in your tiles for new ones (but you lose your turn).
* You can use a blank tile for any letter. (0 points for blank letters)
* The game ends when all the tiles have been used. If you have tiles left, count up their point values and subtract them from your score.
* The player with the most points wins.
Point system:
A = 1 point
B = 3 points
C = 3 points
D = 2 points
E = 1 point
F = 4 points
G = 2 points
H = 4 points
I = 1 point
J = 8 points
K = 5 points
L = 1 point
M = 3 points
N = 1 point
O = 1 point
P = 3 points
Q = 10 points
R = 1 point
S = 1 point
T = 1 point
U = 1 point
V = 4 points
W = 4 points
X = 8 points
Y = 4 points
Z = 10 points
Blank tiles can be used as any letter and have no point value.

## Credits
Developers: [Ryan Mutula, Samuel Marimbi, Natasha Makungu, Molly Muthama]

## License
This project is open-source and available under the MIT License.



