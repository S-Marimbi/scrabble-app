from .RackClass import Rack, Tile

class Player:
    def __init__(self, name, tile_bag):
        self.name = name
        self.tile_bag = tile_bag
        self.rack = Rack()
        self.score = 0  # Add a score attribute to track the player's score
        for _ in range(7):  # Assuming each player starts with 7 tiles
            tile_letter = tile_bag.draw_tile()
            self.rack.add_tile(Tile(tile_letter))

    def get_rack_arr(self):
        return self.rack.tiles  # Return the list of tiles in the rack

    def get_rack_str(self):
        return self.rack.get_rack_str()  # Return the string representation of the rack

    def replenish_rack(self):
        while len(self.rack.tiles) < 7 and self.tile_bag.get_remaining_tiles() > 0:
            tile_letter = self.tile_bag.draw_tile()
            self.rack.add_tile(Tile(tile_letter))

    def remove_from_rack(self, tile):
        self.rack.remove_tile(self.rack.tiles.index(tile))

    def update_score(self, score):
        self.score += score  # Method to update the player's score