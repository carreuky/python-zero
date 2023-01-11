import random

class Deck:
    suits = ["H", "D", "C", "S"]
    #for loop to get the number
     # str(make the i a strin no matter what)
    values = [str(i) for i in range(2,11)]+['J','Q', 'K', 'A']
    # Write your code here.
    def __init__(self):
        self.cards = []
        self.fill_deck() #place new cards in the cards

    def fill_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(value+suit) #initalized one

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal(self,n):
        dealt_cards =[]
        for i in range(n):
            if len( self.cards) ==0: #look at the constructor
                break

            card = self.cards.pop()
            dealt_cards.append(card)
        
        return dealt_cards
    
    def sort_by_suit(self):
        cards_by_suit ={'H':[],'D':[],'C':[],'S':[]}

        for card in self.cards: #2D or 4H or 9C'
            suit =card[-1] #gvies letter
            cards_by_suit[suit].append(card)#attach the number

        self.cards=(
            cards_by_suit['H']+
            cards_by_suit['D']+
            cards_by_suit['C']+
            cards_by_suit['S']
        )

    def contains(self,card):
        result = False
        for idx in range(len(self.cards) ):
            if card == self.cards[idx]:
                result = True
        return result

    def copy(self):
        new_deck= Deck()
        new_deck.cards= self.cards[:]
        return new_deck

    def get_cards(self):
        return  self.cards[:]


    def __len__(self):
        return len(self.cards)