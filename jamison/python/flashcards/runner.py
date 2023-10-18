from card import *
from turn import *
from deck import *
from round import *

card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
cards = [card_1, card_2, card_3]
deck = Deck(cards)
round = Round(deck)

def start():
  print(f"Welcome! You're playing with {deck.count()} cards.")
  print("-------------------------------------------------")
  outcome = False
  while outcome == False:
    index = 0
    print(f"This is card number {index + 1} out of {deck.count()}")
    print(f"Question: {round.current_card().question}")
    guess = input()
    turn = round.take_turn(guess)
    print(turn.feedback())
    outcome = True

start()