import unittest
from card import *

class CardTests(unittest.TestCase):

  def test_it_exists(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        isinstance(card, Card)
        self.assertEqual(card.question, "What is the capital of Alaska?")
        self.assertEqual(card.answer, "Juneau")
        self.assertEqual(card.category, "Geography")

if __name__ == '__main__':
  unittest.main()