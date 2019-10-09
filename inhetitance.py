
class Card(object):

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return('%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit]))

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit:
            return(1)
        if self.suit < other.suit:
            return(-1)
        # suits are the same, check ranks
        if self.rank > other.runk:
            return(1)
        if self.rank < other.runk:
            return(-1)
        # ranks are the same
        return(0)


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return('/n'.join(res))

    def pop_card(self):
        return(self.cards.pop())

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        import random
        ramdom.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):

    def __init__(self, lable=''):
        self.cards = []
        self.lable = lable


deck = Deck()
# print(deck)

hand = Hand('new hand')
print(hand)
print(hand.lable)

card = deck.pop_card()
hand.add_card(card)

print(hand)
