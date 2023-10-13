import unittest
from card import *
from turn import *
from deck import *

class TurnTests(unittest.TestCase):

  def test_it_exists(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    isinstance(deck, Deck)
    self.assertEqual(deck.cards, cards)

  def test_count(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    self.assertEqual(deck.count(), 3)

  def test_cards_in_category(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    self.assertEqual(deck.cards_in_category("STEM"), [card_2, card_3])
    self.assertEqual(deck.cards_in_category("Geography"), [card_1])
    self.assertEqual(deck.cards_in_category("Pop Culture"), [])

if __name__ == '__main__':
  unittest.main()