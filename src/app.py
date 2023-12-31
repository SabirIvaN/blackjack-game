#!/usr/bin/env python3

from parties.sets import *;
from scripts.bets import *;
from scripts.hits import *;
from scripts.cards import *;
from scripts.pushes import *;
from scripts.dealers import *;
from scripts.players import *;

playing = True

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    # Create & deal two cards to player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Create & deal two cards to dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    take_bet(player_chips) # Prompt the Player for their bet
    show_some(player_hand, dealer_hand) # Show cards (but keep one dealer card hidden)

     # Recall this variable from our hit_or_stand function
    while playing:
        hit_or_stand(deck, player_hand) # Prompt for Player to Hit or Stand
        show_some(player_hand, dealer_hand) # Show cards (but keep one dealer card hidden)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand) # Takes hits from the dealer

        show_all(player_hand, dealer_hand) # Show all cards

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n'")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
