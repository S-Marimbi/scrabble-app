#initializing the game
#initializing the board, tile bag and players
#function to start the game
def start_game():
    board = initialize_board()
    tile_bag = initialize_tile_bag()
    players = [Player('Human', tile_bag), Player('Computer', tile_bag)]
    current_player = 0
    return board, tile_bag, players, current_player          