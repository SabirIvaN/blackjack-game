# Function to display some cards
def show_some(player, dealer):
    print("\nDealer's hand: ")
    print("<card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep="\n")

# Function to display all cards
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep = "\n")
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep = "\n")
    print("Player's Hand = ", player.value)