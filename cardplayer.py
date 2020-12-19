from cardpile import CardPile
from card import Card

class CardPlayer:
    """ Card player in a turn-based card game

    Attributes:
        # drawn: CardPile
        #    card(s) that player has drawn 
        hand: CardPile
            cards that player is currently holding (CardPile)
        isManual: bool
            if true then player requests input when taking turn 
            if false player will automatically take turn
        name: str
            name of player 

    """

    def __init__(self, name: str, isManual = False):
        self.isManual = isManual
        self.name = name
        self.hand = CardPile()
        # self.drawn = CardPile()
    
    @property
    def isManual(self):
        return self._isManual
    
    @isManual.setter
    def isManual(self, value: bool):
        self._isManual = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value


def test_CardPlayer():
    p1 = CardPlayer('Player1',False)
    p2 = CardPlayer('Player2', True)
    p1.hand.add_card(Card('7','d'))
    # p1.drawn.add_card(Card('K','c'))
    print('p1 hand: ', p1.hand.display_cards())
    # print('p1 drawn: ', p1.drawn.display_cards())


if __name__ == '__main__':
    test_CardPlayer()