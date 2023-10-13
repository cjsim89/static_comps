import unittest
from card import *
from turn import *
from deck import *
from round import *

class TurnTests(unittest.TestCase):

  def test_it_exists(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    round = Round(deck)
    isinstance(round, Round)
    self.assertEqual(round.deck, deck)
    self.assertEqual(round.turns, [])
    self.assertEqual(round.current_card(), card_1)

  def test_it_takes_turn(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    round = Round(deck)
    new_turn = round.take_turn("Juneau")
    isinstance(new_turn, Turn)
    self.assertEqual(new_turn.correct(), True)
    self.assertEqual(round.turns, [new_turn])
    self.assertEqual(round.number_correct, 1)
    turn_2 = round.take_turn("Venus")
    self.assertEqual(round.turns, [new_turn, turn_2])
    self.assertEqual(round.turns[1].feedback(), "Incorrect.")


if __name__ == '__main__':
  unittest.main()