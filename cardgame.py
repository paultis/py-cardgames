from card import Card
from cardplayer import CardPlayer
from cardpile import CardPile, standard_deck
import random


class CardGame:
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
    name = 'Basic Card Game'
    turn_over_first_card = True
    max_times_recycling_discard_pile = 5
    times_recycling_discard_pile = 0

    def __init__(self, players, num_cards):
        self.completed = False
        self.curr_player = None
        self.num_cards = num_cards
        self.players = players

    def deal_cards(self, num_cards: int):
        i = 0
        while i < num_cards:
            for p in self.players:
                p.hand.add_card(self.deck.pop_card(0))
            i = i + 1

    def display_game(self):
        print('')
        print(self.name)
        for p in self.players:
            print(p.name + ': ' + p.hand.display_cards())
        if len(self.discard_pile.cards) == 0:
            print('Discard pile: ')
        else:
            print('Discard pile: ' + self.discard_pile.cards[-1].label)
        print('Current turn: ' + self.curr_player.name)

    def draw_card(self, player: CardPlayer):

        card = self.deck.pop_card(0)
        player.hand.add_card(card)
        print(player.name + ' draws a card')
        if len(self.deck.cards) == 0:
            if self.times_recycling_discard_pile < self.max_times_recycling_discard_pile:
                self.recycle_discard_pile()
                self.times_recycling_discard_pile += 1
            else:
                self.completed = True
                print('Recycled discard pile ' + str(self.times_recycling_discard_pile) + ' times.  Game over.')
        return card

    def find_playable_cards(self, player: CardPlayer):
        # For this basic card game, all cards in the player's hand can be played
        return player.hand

    def get_next_player(self):
        if len(self.players) == 0:
            return None
        if self.curr_player is None:
            return self.players[0]
        else: 
            curr_pos = self.players.index(self.curr_player)
            next_pos = curr_pos + 1
            if next_pos == len(self.players):
                next_pos = 0
            return self.players[next_pos]

    def play_card(self, card: Card, player: CardPlayer):
        self.discard_pile.add_card(card, source_pile=player.hand)
        print(player.name + ' plays ' + card.label)

    def play_game(self):
        while not self.completed:
            self.play_turn()
            self.curr_player = self.get_next_player()
            self.display_game()
            self.update_status()
        print('Game over')

    def play_turn(self):
        if self.curr_player.isManual:
            self.play_turn_manual()
        else:
            self.play_turn_auto()

    def play_turn_auto(self):
        # Strategy - Here the random strategy is play a card from the hand 80% of the time, and draw the other 20%
        choices = [1,2,3,4,5]
        random.shuffle(choices)
        choice = choices[0]
        # Draw a card from the deck
        if choice == 1:
            card = self.draw_card(self.curr_player)
            print(self.curr_player.name + ' draws ' + card.label)
        # Play a card from the hand - in this case it goes on the discard pile
        else:
            # card = self.curr_player.hand.pop_card(0)
            playable_cards = self.find_playable_cards(self.curr_player)
            card = self.select_card_to_play(self.curr_player, playable_cards)
            self.play_card(card, self.curr_player)
            print('play_turn_auto: ' + self.curr_player.name + ' discards ' + card.label)
        return

    def play_turn_manual(self):
        return
    
    def recycle_discard_pile(self):
        # Move all cards from discard pile to deck except for top card
        topcard = self.discard_pile.pop_card(0)
        for c in self.discard_pile.cards:
            self.discard_pile.remove_card(c, target_pile=self.deck)
        self.discard_pile.add_card(topcard)
        # Shuffle the deck
        random.shuffle(self.deck.cards)
        return

    def select_card_to_play(self, player: CardPlayer, playable_cards: CardPile):
        # For this basic card game, just select the first one
        if len(playable_cards.cards) > 0:
            card = playable_cards.pop_card(0)
            return card
        else:
            return None

    def setup_game(self):
        # Create a new deck
        self.deck = standard_deck()
        self.deck.shuffle_cards()
        # Make sure discard pile and player hands are cleared
        self.discard_pile = CardPile(visible = True)
        for p in self.players:
            p.hand = CardPile()
        # Deal cards and determine first player
        self.deal_cards(self.num_cards)
        if self.turn_over_first_card:
            card = self.deck.pop_card(0)
            self.discard_pile.add_card(card)
        self.curr_player = self.players[0]
        # self.display_game()

    def update_status(self):
        # Check to see if game is complete - here the check is for which player has no cards left
        for p in self.players:
            if len(p.hand.cards) == 0:
                print(p.name + ' has no cards left. ' + p.name + ' is the winner!')
                self.completed = True
                return
        return
        

def test_CardGame():
    p1 = CardPlayer('p1')
    p2 = CardPlayer('p2')
    p3 = CardPlayer('p3')

    game = CardGame(players = [p1,p2,p3], num_cards=5)
    game.setup_game()
    game.display_game()
    game.play_game()


if __name__ == '__main__':
    test_CardGame()



