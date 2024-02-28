from turn import *

class Round:

  def __init__(self, deck):
    self.deck = deck
    self.turns = []
    # self.answered_cards = []
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
  
  def turn_categories(self):
    categories = {}
    for turn in self.turns:
      if categories.get(turn.card.category):
        categories[turn.card.category] += 1
      else:
        categories[turn.card.category] = 1
    return categories
  
  def correct_by_category(self):
    correct_category_turns = {}
    for turn in self.turns:
      if turn.correct() == True:
        if correct_category_turns.get(turn.card.category):
          correct_category_turns[turn.card.category] += 1
        else:
          correct_category_turns[turn.card.category] = 1
      else:
        if not correct_category_turns.get(turn.card.category):
          correct_category_turns[turn.card.category] = 0
    for category, num_correct in correct_category_turns.items():
      total_for_cat = self.turn_categories()[category]
      percentage = num_correct / total_for_cat
      print(f"{category} - {percentage}% correct")