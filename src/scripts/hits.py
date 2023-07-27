# Function for taking hits
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Function prompting the Player to Hit or Stand
def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'...")
        if x[0].lower() == "h":
            hit(deck, hand)
        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing.")
        else:
            print("Sorry, please try again.")
            continue
        break
