from card import Card, SUIT_DICT, CARD_DICT
import random

class CardPile:
    """ Pile of cards

    Can be used to represent a deck, a hand, a discard pile, or a set of played cards 

    Attributes:
        cards:  
            collection of Card objects
        visible:
            if true, each Card is visible to all players

    """

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value
    
    @property
    def visible(self):
        return self._visible
    
    @visible.setter
    def visible(self, value: bool):
        self._visible = value

    def __init__(self, visible = False):
        self.cards = []
        self.visible = visible

    def add_card(self, card: Card, source_pile = None):
        c = card
        if source_pile:
            # Check if the source pile has a matching card and remove if it does
            c = source_pile.contains_card(card)
            if c:
                source_pile.remove_card(c)
            # If source pile doesn't have matching card, then return None 
            else:
                return None
        # After removing card from source pile, add it to this card pile
        self.cards.append(c)
        return c

    def contains_card(self, card: Card):
        # Check if any card in the pile matches a particular card value (e.g. '7c')
        # If so, return a reference to the matching card in the pile
        for c in self.cards:
            if c == card: 
                return c
        return None

    def count_by_suit(self, suits = ['c','d','h','s']):
        # Returns a dictionary with suit and count of cards
        # Example: count_by_suit(['c','d','h','s']) 
        suit_count = dict()
        for s in suits:
            suit_count[s] = 0
        for c in self.cards:
            suit_count[c.suit] = suit_count.get(c.suit,0) + 1 
        return suit_count

    def display_cards(self):
        s = ''
        for c in self.cards:
            s = s + c.label + ' '
        return s

    def extract_cards(self, faces):
        # Get cards that match a set of faces - also returns the remaining cards
        # Example: extract_cards(['A', '8'], [Card(Ah), Card(8c), Card(Ks), Card(4h)])
        # returns match = [Card(Ah), Card(8c)] and remainder = [Card(Ks), Card(4h)]
        match = CardPile()
        remainder = CardPile()
        for c in self.cards:
            for f in faces:
                if c.face == f:
                    match.add_card(c)
                else:
                    remainder.add_card(c)
        return (match, remainder)

    def get_highest_card_by_suit(self, suits = ['c','d','h','s']):
        # Returns dictionary with highest ranking card in each suit
        suit_rank = dict()
        for s in suits:
            suit_rank[s] = 0
        for c in self.cards:
            if c.rank > suit_rank[c.suit]:
                suit_rank[c.suit] = c.rank
        return suit_rank

    def pop_card(self, pos: int):
        if len(self.cards) >= pos + 1:
            return self.cards.pop(pos)
        else:
            return None

    def remove_card(self, card: Card, target_pile = None):
        c = self.contains_card(card)
        if c:
            self.cards.remove(c)
            if target_pile:
                target_pile.add_card(c)
        else:
            return None
        return c

    def shuffle_cards(self):
        random.shuffle(self.cards)


def standard_deck():
    # Create standard deck
    deck = CardPile()
    for s in SUIT_DICT.keys():
        for c in CARD_DICT.keys():
            card = Card(c,s)
            deck.add_card(card)
    return deck


def test_CardPile():
    cp = CardPile()
    cp2 = CardPile()
    c1 = Card('A','c')
    c2 = Card('K','d')
    c3 = Card('7','s')
    c4 = Card('7','c')
    cp.add_card(c1)
    cp.add_card(c2)
    cp2.add_card(c3)
    print('hand1 ' + cp.display_cards())
    print('hand2 ' + cp2.display_cards())
    cp.remove_card(c1,cp2)
    print('hand1 ' + cp.display_cards())
    print('hand2 ' + cp2.display_cards())
    cp.add_card(c1,cp2)
    print('hand1 ' + cp.display_cards())
    print('hand2 ' + cp2.display_cards())
    if cp2.contains_card(c4):
        print('hand2 contains ' + c4.label)
        print('removing ' + c4.label)
        cp2.remove_card(c4,cp)
    else:
        print('hand2 does not contain ' + c4.label)
    print('hand1 ' + cp.display_cards())
    print('hand2 ' + cp2.display_cards())
    deck = standard_deck()
    print('deck ' + deck.display_cards())
    deck.shuffle_cards()
    print('deck ' + deck.display_cards())
    top_card = deck.pop_card(0)
    print('top card ' + top_card.label)
    print('deck ' + deck.display_cards())
    pile = CardPile()
    pile.add_card(c1)
    pile.add_card(c2)
    pile.add_card(c3)
    pile.add_card(c4)
    sevens, non_sevens = pile.extract_cards(['7'])
    print('pile: ' + pile.display_cards())
    print('sevens: ' + sevens.display_cards())
    print('non-sevens: ' + non_sevens.display_cards())

    suits = pile.count_by_suit()    
    print('suits: ', suits)

    ranks = pile.get_highest_card_by_suit()
    print('ranks ', ranks)

    
if __name__ == '__main__':
    test_CardPile()