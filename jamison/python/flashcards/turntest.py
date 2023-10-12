import unittest
from card import *
from turn import *

class TurnTests(unittest.TestCase):

  def test_it_exists(self):
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)
    isinstance(turn, Turn)
    self.assertEqual(turn.guess, "Juneau")
    self.assertEqual(turn.card, card)

  def test_correct(self):
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)
    self.assertTrue(turn.correct())

  def test_incorrect(self):
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Austin", card)
    self.assertFalse(turn.correct())

  def test_feedback(self):
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)
    self.assertEqual(turn.feedback(), "Correct!")
    turn_2 = Turn("Austin", card)
    self.assertEqual(turn_2.feedback(), "Incorrect.")

if __name__ == '__main__':
  unittest.main()