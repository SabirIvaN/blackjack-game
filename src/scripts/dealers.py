# The dealer_busts function gives a boost to the dealer
def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.lose_bet()
    
# The dealer_wins feature gives the dealer the win
def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()
