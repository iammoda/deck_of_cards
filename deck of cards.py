import random
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def showCard(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.showCard()

    def shuffle(self):
        #start at index 51 and decrement by 1 till 0.
        for i in range(len(self.cards)-1, 0, -1 ):
            r = random.randint(0, i)
            self.cards [i], self.cards [r] = self.cards[r]. self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.showCard()

    def discard(self):
        return self.hand.pop()

