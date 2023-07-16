# Import Random library
import random;

# Card suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Card ranks
ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'
    )

# The value of card values
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 
    'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }

# The Card class initiates a card with the given suit and rank.
class Card:
    # Card class constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # String representation of the Card object
    def __str__(self):
        return self.rank + " of " + self.suit

# The Deck class will create a deck from the given cards.
class Deck:
    # Deck class constructor
    def __init__(self):
        self.deck = [] # Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) # Build Card objects and add them to the list
    # String representation of the Deck object
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp
    # The Shuffle function will shuffle the entire deck
    def shuffle(self):
        random.shuffle(self.deck)
    # The Deal function will draw one card from the deck
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
# The hand class adds cards from the deck class to the player's hand.
class Hand:
    # Hand class constructor
    def __init__(self):
        self.cards = [] # Start with an empty list as we did in the Deck class
        self.value = 0 # Start with zero value
        self.aces = 0 # Add an attribute to keep track of aces
    # The add_card function will add a card to the player's hand.
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
    # Since an ace can have two values: 1 or 11, the adjust_for_ace function will change the value of the ace.
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# The Chips class keeps track of a player's starting chips, stakes, and current winnings.
class Chips:
    # Chips class constructor
    def __init__(self):
        self.total = 100 # This can be set to a default value or supplied by a user input
        self.bet = 0
    # The win_bet function adds a win
    def win_bet(self):
        self.total += self.bet
    # The lose_bet function takes away winnings
    def lose_bet(self):
        self.total -= self.bet