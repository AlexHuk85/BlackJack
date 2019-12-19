import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# class for single card object
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# class for deck object
class Deck():

    def __init__(self):
        # list to hold 52 cards
        self.deck = []

        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card)
    
    def __str__(self): # for display all cards
        
        self.string = ''

        for i in self.deck:
            self.string += i.__str__()+'\n'
        
        return self.string
    
    def shuffle(self): # for shuffle deck

        random.shuffle(self.deck)

    def give_card(self):
        card = self.deck.pop()

        return card

# Hand class
class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        # return self.value # <-- this line for debug

    def adjust_ace(self):
        pass

    

# Testing area
test_deck = Deck()
test_deck.shuffle()
#print(test_deck) # <-- print out 52 cards
test_player = Hand()
test_player.add_card(test_deck.give_card())
test_player.add_card(test_deck.give_card())
print(test_player.value)
for card in test_player.cards:
    print(card)