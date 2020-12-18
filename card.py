SUIT_DICT = {
    "c": {"name": "clubs", "rank": 1},
    "d": {"name": "diamonds", "rank": 2},
    "h": {"name": "hearts", "rank": 3},
    "s": {"name": "spades", "rank": 4}
}

CARD_DICT = {
    "A": {"name": "Ace", "rank": 1},
    "2": {"name": "Two", "rank": 2},
    "3": {"name": "Three", "rank": 3},
    "4": {"name": "Four", "rank": 4},
    "5": {"name": "Five", "rank": 5},
    "6": {"name": "Six", "rank": 6},
    "7": {"name": "Seven", "rank": 7},
    "8": {"name": "Eight", "rank": 8},
    "9": {"name": "Nine", "rank": 9},
    "T": {"name": "Ten", "rank": 10},
    "J": {"name": "Jack", "rank": 11},
    "Q": {"name": "Queen", "rank": 12},
    "K": {"name": "King", "rank": 13}
}

class Card:
    """ A standard playing card

    Attributes:
        face:  
            A,2,3,4,5,6,7,8,9,T,J,Q,K
        suit: 
            c = clubs
            d = diamonds
            h = hearts
            s = spades
        rank: rank of card
            A-9 = 1..9
            T-K = 10..13
        label: short name of card
            Examples: Ad = ace of diamonds, 7c = seven of clubs

    """
    
    def __init__(self, face: str, suit: str):
        self.face = face
        self.suit = suit
    
    @property
    def face(self):
        return self._face
    
    @face.setter
    def face(self, value):
        if value.capitalize() not in CARD_DICT.keys():
            raise ValueError('Card not allowed: ' + face)
        self._face = value.capitalize()

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if value.lower() not in SUIT_DICT.keys():
            raise ValueError('Suit not allowed: ' + suit)
        self._suit = value.lower()

    @property
    def rank(self):
        return CARD_DICT[self.name]['rank']

    @property
    def label(self):
        return self.face + self.suit

    def __eq__(self, other):
        return (self.face == other.face and self.suit == other.suit)

    def __ne__(self, other):
        return not self.__eq__(other)

def test_Card():
    c1 = Card('7','d')
    c2 = Card('7','d')
    c3 = Card('7','c')

    print('c1 = ' + c1.label + ' c2 = ' + c2.label + ' c3 = ' + c3.label)
    print('c1 is c2: ' + str(c1 is c2))
    print('c1 == c2: ' + str(c1 == c2))
    print('c1 != c2: ' + str(c1 != c2))
    print('c2 == c3: ' + str(c2 == c3))

# test_Card()