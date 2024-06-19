from lib.TileBag import Bag, tile_distribution
from lib.BoardClass import Board
from lib.PlayerClass import Player
from lib.endgame import game_over, display_final_scores, declare_winner
import random

# Load the word list from dictionary.txt
def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip().upper() for line in file]

# Validate if a word is in the dictionary
def is_valid_word(word, word_list):
    return word in word_list

# Generate a valid random word from the computer's rack
def generate_computer_word(rack, word_list):
    rack_letters = [tile.get_letter() for tile in rack]
    random.shuffle(rack_letters)
    for word in word_list:
        if all(rack_letters.count(char) >= word.count(char) for char in word):
            return word
    return None

# Generate a hint for the human player
def generate_hint(rack, word_list):
    rack_letters = [tile.get_letter() for tile in rack]
    for word in word_list:
        if all(rack_letters.count(char) >= word.count(char) for char in word):
            return word
    return None

def check_valid_placement(word, position, direction, board, rack_arr, is_human_turn):
    row, col = position
    score = 0
    word_length = len(word)
    if direction not in ['right', 'down']:
        return False, 0

    if (direction == 'right' and col + word_length > 15) or (direction == 'down' and row + word_length > 15):
        return False, 0

    # Ensure connection to existing tiles
    connects = False
    temp_rack_arr = list(rack_arr)

    for i, letter in enumerate(word):
        new_row, new_col = (row, col + i) if direction == 'right' else (row + i, col)
        if board.board[new_row][new_col].strip():  # Check if the board position is not empty
            if board.board[new_row][new_col].strip() != letter:
                return False, 0
            connects = True
        else:
            if letter not in temp_rack_arr:
                return False, 0
            temp_rack_arr.remove(letter)
            score += ord(letter) - ord('A') + 1

    if is_human_turn and not connects and not board.board[7][7].strip():  # Human must start from center star
        return False, 0
        

    if not is_human_turn and not connects:
        # Check if the computer connects to any existing human tile
        connects_to_human_tile = False
        for i, letter in enumerate(word):
            new_row, new_col = (row, col + i) if direction == 'right' else (row + i, col)
            if new_row == 7 and new_col == 7:  # Center star is always considered connected
                connects_to_human_tile = True
                break
            if new_row > 0 and board.board[new_row - 1][new_col].strip():  # Check tile above
                connects_to_human_tile = True
                break
            if new_row < 14 and board.board[new_row + 1][new_col].strip():  # Check tile below
                connects_to_human_tile = True
                break
            if new_col > 0 and board.board[new_row][new_col - 1].strip():  # Check tile to the left
                connects_to_human_tile = True
                break
            if new_col < 14 and board.board[new_row][new_col + 1].strip():  # Check tile to the right
                connects_to_human_tile = True
                break
        
        if not connects_to_human_tile:
            return False, 0

    return True, score


def main():
    # Load words from the dictionary.txt
    word_list = load_words("dictionary.txt")  
    tile_bag = Bag(tile_distribution)
    board = Board()
    # Create players
    human_player = Player("Human", tile_bag)
    computer_player = Player("Computer", tile_bag)
    # List of players
    players = [human_player, computer_player]
    # Start with the first player (index 0)
    current_player_index = 0
    # Initialize pass count to track consecutive passes
    pass_count = [0]  # Using a list to keep track of pass count

    # Display the current state of the game
    def print_game_state():
        print("Current Board:")
        print(board.get_board())
        print(f"Human's hand: {human_player.get_rack_str()}")
        print(f"Computer's hand: {computer_player.get_rack_str()}")
        print(f"Remaining tiles in bag: {tile_bag.get_remaining_tiles()}")

    # Human player's turn with an option to pass a play turn or request for a hint
    def human_turn():
        print("Human's turn")
        print_game_state()
        while True:
           action = input("Enter 'P' to pass, 'H' for a hint, or any word to play: ").upper()
           if action == 'P':
            pass_count[0] += 1
            return 'pass'
           elif action == 'H':
            hint = generate_hint(human_player.get_rack_arr(), word_list)
            print(f"Hint: try to form a word with these letters - {hint}")
           else:
            word = action
            if not is_valid_word(word, word_list):
                print("Invalid word. Please try again.")
                continue
            direction = input("Enter direction (right/down): ").lower()
            row = int(input("Enter starting row (0-14): "))
            col = int(input("Enter starting column (0-14): "))
            
            if row != 7 or col != 7:
                print("You must start from the center tile (row 7, column 7). Please try again.")
                continue
            
            board.place_word(word, (row, col), direction, human_player)
            pass_count[0] = 0
            return 'played'


    # Human player's turn with an option to pass a play turn or request for a hint
    def computer_turn():
        print("Computer's turn")
        rack_arr = computer_player.get_rack_arr()
        word = generate_computer_word(rack_arr, word_list)
        if word:
            word_length = len(word)
            valid_placement = False
            attempts = 0

            while not valid_placement and attempts < 100:  # Avoid infinite loops
                direction = random.choice(['right', 'down'])
                row = random.randint(0, 14)
                col = random.randint(0, 14)

                # Check if the word fits on the board
                if direction == 'right' and col + word_length <= 15:
                    valid_placement = True
                elif direction == 'down' and row + word_length <= 15:
                    valid_placement = True

                attempts += 1

            # Place the word on the board
            if valid_placement:
                board.place_word(word, (row, col), direction, computer_player)
                print(f"Computer placed: {word} at ({row}, {col}) {direction}")
                pass_count[0] = 0
                return 'played'
            else:
                # Computer could not find a valid placement
                print("Computer could not find a valid position to place the word.")
                pass_count[0] += 1
                return 'pass'
        else:
            # Computer could not find a valid word
            print("Computer could not find a valid word to play.")
            pass_count[0] += 1
            return 'pass'

    # Checking game conditions
    while True:
        current_player = players[current_player_index]
        if current_player == human_player:
            human_turn()
        else:
            computer_turn()

        # Check for game over conditions
        if pass_count [0] >= 2:
            print("Both players passed. Game over!")
            break

        if tile_bag.get_remaining_tiles() == 0 and (not human_player.get_rack_arr() or not computer_player.get_rack_arr()):
            print("Game over!")
            break

        # Switch turns
        current_player_index = 1 - current_player_index

        print_game_state()

    # End game and declare winner
    display_final_scores(players)
    declare_winner(players)

if __name__ == "__main__":
    main()
