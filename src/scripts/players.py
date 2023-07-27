# The player_busts function gives a boost to the player
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

# The player_busts function gives the player a win
def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()
