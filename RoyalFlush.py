import numpy
import random


start_deck = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks', 'as',
             '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 'ad',
             '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh', 'ah',
             '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 'ac']

suits = ["hearts", "diamonds", "spades", "clubs"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

start_deck2=[]




print(start_deck2)

# Set starting parameters
deck = start_deck.copy()
hand = []
required_cards = ['2s', '3s', '4s', '5s', '6s']
length_hand_needed = len(required_cards)
deals = 0
wins = 0
# print(deck)
cards_in_deck_start = len(deck)
cards_in_deck = cards_in_deck_start
hand_cards = 0

# while wins < 10:
while wins < 100:
    # Generate random card index to remove from hand and pop out card. Depreciate length of deck by 1 for each card pulled.
    card_picked_index = int(cards_in_deck * random.random())
    # print(card_picked_index)
    new_card = deck.pop(card_picked_index)
    # print(new_card)
    # print(deck)
    # deck.pop(card_picked_index)
    cards_in_deck -= 1
    # Test if pulled card is in the required card list.

    # required_cards =
    if new_card in required_cards:
        hand.append(new_card) # Add new card to hand
        # print(hand)
        hand_cards += 1
        # If len is 5 (or length of defined required card list) record a win and restart the deck.
        if hand_cards == length_hand_needed:
            print(hand)
            print('win!')
            wins += 1; deals += 1; hand_cards = 0
            cards_in_deck = cards_in_deck_start
            deck = start_deck.copy()
            hand = []
    # If card is not in required list, reset hand and deck.
    else:
         hand = []
         deals += 1
         cards_in_deck = cards_in_deck_start
         deck = start_deck.copy()
         hand_cards = 0

print(deals)
print(wins)
prob = wins / deals
print(prob)

theoretical_prob = (5/52) * (4/51) * (3/50) * (2/49) * (1/48)

print(theoretical_prob)
