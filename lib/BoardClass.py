import os
from .logic import calculate_word_score

class Board:
    """
    Creates the Scrabble board.
    """
    def __init__(self):
        # Creates a 2-dimensional array that serves as the board, 
        # as well as adds in the premium squares.
        self.board = [["   " for _ in range(15)] for _ in range(15)]
        self.add_premium_squares()
        self.board[7][7] = "  X "  # Center star where the first word must cross

    def get_board(self):
        # Define the width of each cell for consistent alignment
        cell_width = 5  # Adjust as needed based on your board content

        # Prepare a header row with column numbers
        header = "     " + " | ".join(f"{i:<{cell_width}}" for i in range(15))
        separator = "  " + "+".join("-" * (cell_width + 1) for _ in range(15))

        # Initialize board_str with the header and separator
        board_str = header + "\n" + separator + "\n"

        # Iterate through each row of the board
        for i in range(15):
 
        # Construct the row header (row number) and content with cell values
            row_header = f"{i:<2} | "
            row_content = " | ".join(f"{self.board[i][j]:<{cell_width}}" for j in range(15))
            row_str = row_header + row_content

        # Append the row to board_str
            board_str += row_str + "\n"

        # Add separator after each row (including the last one)
            board_str += separator + "\n"           

            

        return board_str
 
    def add_premium_squares(self):
        """
         Adds all of the premium squares that influence the word's score.
         TWS- Triple Word Score
         DWS- Double Word Score
         TLS- Triple Letter Score
         DLS- Double Letter Score
        """
        premium_squares = {
            (0, 0): "TWS", (7, 0): "TWS", (14, 0): "TWS",
            (0, 7): "TWS", (14, 7): "TWS", (0, 14): "TWS",
            (7, 14): "TWS", (14, 14): "TWS",
            (1, 1): "DWS", (2, 2): "DWS", (3, 3): "DWS", (4, 4): "DWS",
            (1, 13): "DWS", (2, 12): "DWS", (3, 11): "DWS", (4, 10): "DWS",
            (13, 1): "DWS", (12, 2): "DWS", (11, 3): "DWS", (10, 4): "DWS",
            (13, 13): "DWS", (12, 12): "DWS", (11, 11): "DWS", (10, 10): "DWS",
            (1, 5): "TLS", (1, 9): "TLS", (5, 1): "TLS", (5, 5): "TLS",
            (5, 9): "TLS", (5, 13): "TLS", (9, 1): "TLS", (9, 5): "TLS",
            (9, 9): "TLS", (9, 13): "TLS", (13, 5): "TLS", (13, 9): "TLS",
            (0, 3): "DLS", (0, 11): "DLS", (2, 6): "DLS", (2, 8): "DLS",
            (3, 0): "DLS", (3, 7): "DLS", (3, 14): "DLS", (6, 2): "DLS",
            (6, 6): "DLS", (6, 8): "DLS", (6, 12): "DLS", (7, 3): "DLS",
            (7, 11): "DLS", (8, 2): "DLS", (8, 6): "DLS", (8, 8): "DLS",
            (8, 12): "DLS", (11, 0): "DLS", (11, 7): "DLS", (11, 14): "DLS",
            (12, 6): "DLS", (12, 8): "DLS", (14, 3): "DLS", (14, 11): "DLS"
        }
        for (x, y), value in premium_squares.items():
            self.board[x][y] = f" {value} "

    def is_valid_placement(self, word, location, direction, first_turn):
        x, y = location
        if direction not in ["right", "down"]:
            return False

        if first_turn:
            if direction == "right":
                if not (y <= 7 < y + len(word)):
                    return False
            elif direction == "down":
                if not (x <= 7 < x + len(word)):
                    return False

        for i, letter in enumerate(word):
            if direction == "right":
                if y + i >= 15 or (self.board[x][y + i].strip() and self.board[x][y + i].strip() != letter):
                    return False
            elif direction == "down":
                if x + i >= 15 or (self.board[x + i][y].strip() and self.board[x + i][y].strip() != letter):
                    return False
        return self.check_adjacent_words(word, location, direction)

    def check_adjacent_words(self, word, location, direction):
        x, y = location
        for i, letter in enumerate(word):
            adj_x, adj_y = (x, y + i) if direction == "right" else (x + i, y)
            if direction == "right":
                if (adj_x > 0 and self.board[adj_x - 1][adj_y].strip()) or (adj_x < 14 and self.board[adj_x + 1][adj_y].strip()):
                    return True
            elif direction == "down":
                if (adj_y > 0 and self.board[adj_x][adj_y - 1].strip()) or (adj_y < 14 and self.board[adj_x][adj_y + 1].strip()):
                    return True
        return False

    def can_place_word(self, word, location, direction):
        x, y = location
        if direction not in ["right", "down"]:
            return False

        for i, letter in enumerate(word):
            if direction == "right":
                if y + i >= 15 or (self.board[x][y + i].strip() and self.board[x][y + i].strip() != letter):
                    return False
            elif direction == "down":
                if x + i >= 15 or (self.board[x + i][y].strip() and self.board[x + i][y].strip() != letter):
                    return False
        return True

    def place_word(self, word, location, direction, player):
        x, y = location
        for i, letter in enumerate(word):
            if direction == "right":
                self.board[x][y + i] = f" {letter} "
            elif direction == "down":
                self.board[x + i][y] = f" {letter} "

        # Calculate the score for the placed word
        special_tiles = {}  # Add logic to handle special tiles if needed
        word_score = calculate_word_score(word, special_tiles)
        player.update_score(word_score)

        # Removes tiles from player's rack and replaces them with tiles from the bag.
        for letter in word:
            for tile in player.get_rack_arr():
                if tile.get_letter() == letter:
                    player.remove_from_rack(tile)
        player.replenish_rack()


   
