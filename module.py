import random
############################################################################################################# CARD CLASS


class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        # print("{} of {}".format(self.value, self.suit))
        return "{} of {}".format(self.value, self.suit)

    def display(self):
        a = 0
        suit_line = 0
        if self.suit == "Hearts":
            suit_line = f"|  {self.suit}  |"

        if self.suit == "Spades":
            suit_line = f"|  {self.suit}  |"

        if self.suit == "Clubs":
            suit_line = f"|  {self.suit}   |"

        if self.suit == "Diamonds":
            suit_line = f"| {self.suit} |"

        if self.value == "2" or self.value == "3" or self.value == "4" \
                           or self.value == "5" or self.value == "6" or self.value == "7" \
                           or self.value == "8" or self.value == "9":
            a = f" ----------\n|          |\n|    {self.value}     |\n|    of    |\n{suit_line}\n|          |\n ----------"

        if self.value == "10":
            a = f" ----------\n|          |\n|    {self.value}    |\n|    of    |\n{suit_line}\n|          |\n ----------"

        if self.value == "11":
            a = f" ----------\n|          |\n|   Jack   |\n|    of    |\n{suit_line}\n|          |\n ----------"

        if self.value == "12":
            a = f" ----------\n|          |\n|  Queen   |\n|    of    |\n{suit_line}\n|          |\n ----------"

        if self.value == "13":
            a = f" ----------\n|          |\n|   King   |\n|    of    |\n{suit_line}\n|          |\n ----------"

        if self.value == "14":
            a = f" ----------\n|          |\n|   Ace    |\n|    of    |\n{suit_line}\n|          |\n ----------"

        return a
#################################################################################################### DECK OF CARDS CLASS


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def to_list(self):
        all_cards = []
        for card in self.cards:
            card = card.show()
            all_cards.append(card)
        return all_cards
########################################################################################################### PLAYER CLASS


class Player:
    def __init__(self, name, password):
        self.coins = []
        self.name = name
        self.password = password

    def __str__(self):
        return f"{self.score},{self.name},{self.password}"
############################################################################################################ TABLE CLASS


class Table:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
