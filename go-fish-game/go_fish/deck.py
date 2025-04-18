import random
from card import Card

# Represents a standard deck of 52 playing cards
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    # Shuffles the deck using Fisher-Yates algorithm
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # Draws the top card from the deck
    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None