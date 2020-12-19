from card import Card
from cardpile import CardPile
from cardgame import CardGame, test_CardGame
from cardplayer import CardPlayer


class CrazyEights(CardGame):
    """ A turn-based card game

    Common logic for setting up players

    Attributes:
        completed: bool
            if true, then game is completed and no more turns are necessary
        curr_player: CardPlayer
            player with current turn
        deck: CardPile
            collection of Cards
        name: str
            name of the game being played
        num_cards: int
            number of cards to be dealt to each player
        players: CardPlayer[]
            collection of CardPlayers
    """
    name = 'Crazy Eights'
    current_suit = None

    def display_game(self):
        super().display_game()
        print('Current suit: ' + self.current_suit)

    def find_playable_cards(self, player):
        # Find cards with same rank
        playable_cards = CardPile()
        current_rank = self.discard_pile.cards[-1].rank
        for card in player.hand.cards:
            if (card.rank == current_rank) or (card.suit == self.current_suit) or (card.rank == 8):
                playable_cards.add_card(card) 
        return playable_cards

    def play_card(self, card: Card, player: CardPlayer):
        super().play_card(card, player)
        if card.rank == 8:
            self.current_suit = self.select_crazy_eight_suit(self.curr_player)
            print(player.name + ' sets current suit to ' + self.current_suit)
        else:
            self.current_suit = self.discard_pile.cards[-1].suit

    def play_turn_auto(self):
        playable_cards = self.find_playable_cards(self.curr_player)
        if len(playable_cards.cards) == 0:
            self.draw_card(self.curr_player)
        else:
            card = self.select_card_to_play(self.curr_player, playable_cards)
            self.play_card(card, self.curr_player)

    def select_card_to_play(self, player, playable_cards):
        if len(playable_cards.cards) == 1:
            return playable_cards.cards[0]
        else:
            # Break into eights and non-eights
            eights, non_eights = playable_cards.extract_cards(['8'])
            # If only eights are left, use the first one
            if len(non_eights.cards) == 0:
                return eights.cards[0]
            else: 
                # Further break non-eights into suits
                suits = non_eights.count_by_suit()
                # Then evaluate which card to play:
                #     - most cards in the suit
                #     - if same number cards in suit, then highest rank card 
                card = non_eights.cards[0] # start with first card
                for c in non_eights.cards:
                    if suits[c.suit] > suits[card.suit]:
                        card = c
                    if suits[c.suit] == suits[card.suit]:
                        if c.rank > card.rank:
                            card = c
                return card

    def select_crazy_eight_suit(self, player:CardPlayer):
        # Select the right suit to call when playing a 'crazy eight'
        # Ignore the eights in the hand
        eights, non_eights = player.hand.extract_cards(['8'])
        suits = non_eights.count_by_suit()
        ranks = non_eights.get_highest_card_by_suit()
        suit = 'c'
        # print('Select suit - suits: ' + str(suits) + ' ranks: ' + str(ranks))
        for s in ['d','h','s']:
            if suits[s] > suits[suit]:
                suit = s
            if suits[s] == suits[suit]:
                if ranks[s] > ranks[suit]:
                    suit = s
        return suit

    def setup_game(self):
        super().setup_game()
        self.current_suit = self.discard_pile.cards[-1].suit


def test_CrazyEights():
    p1 = CardPlayer('p1')
    p2 = CardPlayer('p2')
    p3 = CardPlayer('p3')

    game = CrazyEights(players = [p1,p2,p3], num_cards=5)
    game.setup_game()
    game.display_game()
    game.play_game()


if __name__ == '__main__':
    test_CrazyEights()