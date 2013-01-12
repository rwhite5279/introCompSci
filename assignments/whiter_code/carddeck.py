# carddeck.py
""" The carddeck module allows you to work with a deck of cards. By Richard White. 2010-02-17 
There are three attributes to the class Deck:
1. The "shuffle" method, which shuffles the deck of 52 cards
2. The "deal" method, which deals a specified number of cards from the deck
3. The "remaining" instance variable which indicates how many cards are remaining in the deck after dealing

An example of how these attributes may be used is given in the main() program below
"""


import random       # randint    

class Deck:
    """ The Deck class represents a deck of cards that may be shuffled and dealt. """
        

    def __init__(self):     # Create a 52-card deck
        self.num_of_cards = 52
        self.suits = ["Clubs","Diamonds","Hearts","Spades"]
        self.pips = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.shuffle()      # This immediately shuffles the deck so that we can begin dealing right away.
        
    def shuffle(self):      # This is a "method"--it DOES stuff, like shuffle the deck
        """The 'shuffle' method takes the deck of 52 cards and shuffles it."""
        self.unshuffled_deck = range(self.num_of_cards)
        self.shuffled_deck = []
        for i in range(self.num_of_cards):
            self.shuffled_deck.append(self.unshuffled_deck.pop(random.randint(0,len(self.unshuffled_deck)-1)))
            # This takes a random card from the unshuffled deck and pops it into the shuffled deck.
        
    def remaining(self):    # This indicates how many cards are left in the deck
        """The 'remaining' instance variable indicates how may cards are remaining in the deck."""
        return len(self.shuffled_deck)
    
    def deal(self,num_to_deal):
        """The 'deal' method takes the shuffled deck and deals out a specified number of cards from that deck, returning the cards as a list of cards, each card in turn a list including the value (int), the name (string) and the suit (string)."""
        numeric_hand = []     # Will have a numeric list of cards "dealt", from 1 - 52
        pips_hand = []        # Will contain the pips of each card dealt
        suits_hand = []       # Will contain the suits of each card dealt
        cards_hand = []       # Will contain both pips and suits
        if num_to_deal > len(self.shuffled_deck):
            print "Error! Not enough cards remain in deck to deal!"
        else:
            for i in range(num_to_deal):
                # pop a random card from the shuffled deck and place it in numeric hand
                numeric_hand.append(self.shuffled_deck.pop(random.randint(0,len(self.shuffled_deck)-1)))
                # Convert that card number to a card value, Ace through King
                pips_hand.append(self.pips[numeric_hand[i] % 13])
                # Convert the card number to a suit, Club, Diamond, Heart, or Spade
                suits_hand.append(self.suits[numeric_hand[i] / 13])
                # Assemble these cards into a single list, to be returned. The list includes:
                # [0] numeric value of pips (Ace = 1, etc.), [1] string value of pips ("Ace", "Two", etc.),
                # [2] string value of suit ("Hearts", etc.)
                cards_hand.append([numeric_hand[i] % 13 + 1,pips_hand[i],suits_hand[i]])
        return cards_hand

def main():
    mydeck = Deck()         # Create an instance of the Deck object, called mydeck
    mydeck.shuffle()        # Shuffle the deck (although a deck comes preshuffled)
    how_many = input("Enter how many cards you'd like deal to you: ")
    print "Your cards are here in a list, which includes their point value, a string representing their pips, and the suit: "
    print mydeck.deal(how_many)
    print "There are",mydeck.remaining()," cards left in the deck now."
    print "Here, let me deal you a few cards from a Blackjack hand, and we'll see how much your cards total to!"
    myhand = mydeck.deal(3)      # Gets two cards, with info placed in the list myhand
    print "You drew a"
    for i in myhand: print i[1],"of",i[2],"(with a value of",i[0],")"
    total = 0
    for i in myhand:
        if (i[1] in ["Jack","Queen","King"]):
            total = total + 10
        elif i[1] == "Ace":
            total = total + 11
        else:
            total = total + i[0]
    print "Your total in Blackjack (where face cards are worth 10), would be",total
    
if __name__ == "__main__":
    main()
