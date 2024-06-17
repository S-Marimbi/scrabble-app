import random

# Defining the tile bag with quantities
tile_distribution = {
    "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1,
    "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6,
    "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "#": 2  
    # The "#" tile represents a blank tile holding zero points
}

# Container of all the letter tiles in the game
class Bag:
    def __init__(self, tile_distribution):
        self.tiles = self.initialize_tiles(tile_distribution)

    def initialize_tiles(self, tile_distribution):
        # Create a list of tiles based on the distribution
        tiles = []
        for letter, count in tile_distribution.items():
            # Extend the list with the correct number of each letter
            tiles.extend([letter] * count)
            # Shuffle the list of tiles randomly
        random.shuffle(tiles)
        return tiles

    # Draw a tile from the bag
    def draw_tile(self):
        if self.tiles:
            return self.tiles.pop()
        else:
            raise TypeError("Tile bag is empty")

    # Return the number of remaining tiles in the bag
    def get_remaining_tiles(self):
        return len(self.tiles)