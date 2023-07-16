# Function for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would your like to bet?"))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break