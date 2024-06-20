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
        separator = "  " + "+".join("-" * (cell_width + 2) for _ in range(15))

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
         TW- Triple Word Score
         DW- Double Word Score
         TL- Triple Letter Score
         DL- Double Letter Score
        """
        premium_squares = {
            (0, 0): "TW", (7, 0): "TW", (14, 0): "TW",
            (0, 7): "TW", (14, 7): "TW", (0, 14): "TW",
            (7, 14): "TW", (14, 14): "TW",
            (1, 1): "DW", (2, 2): "DW", (3, 3): "DW", (4, 4): "DW",
            (1, 13): "DW", (2, 12): "DW", (3, 11): "DW", (4, 10): "DW",
            (13, 1): "DW", (12, 2): "DW", (11, 3): "DW", (10, 4): "DW",
            (13, 13): "DW", (12, 12): "DW", (11, 11): "DW", (10, 10): "DW",
            (1, 5): "TL", (1, 9): "TL", (5, 1): "TL", (5, 5): "TL",
            (5, 9): "TL", (5, 13): "TL", (9, 1): "TL", (9, 5): "TL",
            (9, 9): "TL", (9, 13): "TL", (13, 5): "TL", (13, 9): "TL",
            (0, 3): "DL", (0, 11): "DL", (2, 6): "DL", (2, 8): "DL",
            (3, 0): "DL", (3, 7): "DL", (3, 14): "DL", (6, 2): "DL",
            (6, 6): "DL", (6, 8): "DL", (6, 12): "DL", (7, 3): "DL",
            (7, 11): "DL", (8, 2): "DL", (8, 6): "DL", (8, 8): "DL",
            (8, 12): "DL", (11, 0): "DL", (11, 7): "DL", (11, 14): "DL",
            (12, 6): "DL", (12, 8): "DL", (14, 3): "DL", (14, 11): "DL"
        }
        for (x, y), value in premium_squares.items():
            self.board[x][y] = f" {value} "

    def is_valid_placement(self, word, location, direction, round_number, first_turn, players):
        x, y = location

        if direction not in ["right", "down"]:
            return "Error: please enter a valid direction."

        current_board_ltr = ""
        needed_tiles = ""

        if first_turn:
            if direction == "right":
                if not (x == 7 and 7 >= y and 7 < y + len(word)):
                    return False
            elif direction == "down":
                if not (y == 7 and 7 >= x and 7 < x + len(word)):
                    return False
                
        # Check if the word overlaps correctly with existing letters on the board
        for i, letter in enumerate(word):
            if direction == "right":
                if y + i >= 15 or (self.board[x][y + i].strip() and self.board[x][y + i].strip() != letter):
                    return "The letters do not overlap correctly, please choose another word."
                current_board_ltr += self.board[x][y + i].strip() or " "
            elif direction == "down":
                if x + i >= 15 or (self.board[x + i][y].strip() and self.board[x + i][y].strip() != letter):
                    return "The letters do not overlap correctly, please choose another word."
                current_board_ltr += self.board[x + i][y].strip() or " "

            if current_board_ltr[i] == " ":
                needed_tiles += letter
            elif current_board_ltr[i] != letter:
                return "The letters do not overlap correctly, please choose another word."

        # Check if the word is in the dictionary
        filename = (r"/scrabble-app/dictionary.txt")
        if word not in filename:
            return "Please enter a valid dictionary word."

        # Check if the player has the required tiles
        player_tiles = players.get_rack_str()
        for letter in needed_tiles:
            if letter not in player_tiles or player_tiles.count(letter) < needed_tiles.count(letter):
                return "You do not have the tiles for this word."

        # Check if the location is out of bounds
        if x > 14 or y > 14 or x < 0 or y < 0 or (direction == "down" and (x + len(word) - 1) > 14) or (direction == "right" and (y + len(word) - 1) > 14):
            return "Location out of bounds."

        # Ensure first turn rule
        if first_turn and location != (7,7):
            return "The first turn must begin at location (7, 7)."

        # Check if the word connects to existing words on the board
        if not first_turn and current_board_ltr == " " * len(word):
            return "Please connect the word to a previously played letter."

        return True  
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


   
