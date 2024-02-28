from turn import *

class Round:

  def __init__(self, deck):
    self.deck = deck
    self.turns = []
    self.number_correct = 0

  def current_card(self):
    return self.deck.cards[0]

  def take_turn(self, guess):
    new_turn = Turn(guess, self.current_card())
    if guess == self.current_card().answer:
      self.number_correct += 1
    self.deck.cards.remove(self.current_card())
    self.turns.append(new_turn)
    return new_turn

  def total_correct_percentage(self):
    if self.number_correct == 0:
      return "0%"
    percentage = self.number_correct / len(self.turns)
    return f"{round(percentage, 2)}%"