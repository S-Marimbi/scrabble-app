from .TileBag import Bag

class Rack:
    def __init__(self):
        self.tiles = []

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remove_tile(self, index):
        return self.tiles.pop(index)

    def get_rack_str(self):
        return ", ".join(map(str, self.tiles))

class Tile:
    def __init__(self, letter):
        self.letter = letter

    def get_letter(self):
        return self.letter

    def __str__(self):
        return self.letter  # Modify this as per your tile representation needs