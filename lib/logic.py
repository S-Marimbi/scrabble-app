# Define the size of the Scrabble board
BOARD_SIZE = 15

# Initialize an empty board
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Function to print the board
def print_board(board):
    for row in board:
        print(' | '.join(row))

# Function to place tiles on the board
def play_turn(word, row, col, direction):
    if direction == 'horizontal':
        for i, letter in enumerate(word):
            board[row][col + i] = letter
    elif direction == 'vertical':
        for i, letter in enumerate(word):
            board[row + i][col] = letter
    else:
        print("Invalid direction. Please choose 'horizontal' or 'vertical'.")

# Example usage
def main():
    # Print empty board
    print("Empty Board:")
    print_board(board)
    
    # Example of placing tiles horizontally
    word_horizontal = "HELLO"
    row_horizontal = 7
    col_horizontal = 6
    direction_horizontal = 'horizontal'
    play_turn(word_horizontal, row_horizontal, col_horizontal, direction_horizontal)
    print("\nBoard after placing tiles horizontally:")
    print_board(board)
    
    # Example of placing tiles vertically
    word_vertical = "WORLD"
    row_vertical = 6
    col_vertical = 8
    direction_vertical = 'vertical'
    play_turn(word_vertical, row_vertical, col_vertical, direction_vertical)
    print("\nBoard after placing tiles vertically:")
    print_board(board)

if __name__ == "__main__":
    main()

# Assign point values to each letter tile
letter_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
    'Z': 10
}

# Function to calculate the score of a word
def calculate_word_score(word, special_tiles):
    score = 0
    for letter in word:
        letter_score = letter_values.get(letter.upper(), 0)
        if letter.upper() in special_tiles:
            letter_score *= special_tiles[letter.upper()]
        score += letter_score
    return score

# Function to calculate the total score for a turn
def calculate_total_score(words, special_tiles):
    total_score = 0
    for word in words:
        total_score += calculate_word_score(word, special_tiles)
    return total_score

# Example usage
def main():
    words = ["HELLO", "WORLD", "PYTHON"]
    special_tiles = {'L': 2, 'D': 3}  # Example of special tiles (double letter for 'L' and triple word for 'D')
    
    total_score = calculate_total_score(words, special_tiles)
    print("Total Score for the turn:", total_score)

if __name__ == "__main__":
    main()