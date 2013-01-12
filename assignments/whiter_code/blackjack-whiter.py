# blackjack.py
"""
This Blackjack program was written by Richard White on 2010-02-22.

IMPROVEMENTS:
* The program is not entirely complete--it only allows the user to play at this point, but enough of the mechanics are there that getting the computer to play as well won't be too difficult.
* The program only plays one round. A more complete version of the program will allow the user to play multiple hands of Craps.
"""
























































# PSEUDOCODE

# 1. Get user's name, give them instructions
# 2. Start playing
# 3. Give user as many cards as they want, and total
# 4. Give computer as many cards as it wants, and total
# 5. Decide who won
# 6. Play again until they don't want to play anymore.




# MORE COMPLETE PSEUDOCODE

# def greeting/instructions

# while (they want to keep playing):
#   1. give user cards
#      a. give 2 cards, display total
#      b. ask if they want more
#      c. keep going until they bust, or don't want anymore cards
#   2. give computer cards
#      a. give 2 cards, display total
#      b. Keep going until it busts, or wins




















































import carddeck           # This module, also written by Richard, should
                          # should be placed in the same directory as
                          # the blackjack.py program

def main():
    name = raw_input("What is your name? ")

    myDeck = carddeck.Deck()
    print "Let's play Blackjack, %s!" % name
    if myDeck.remaining() < 14:
        print "Shuffling"
        myDeck.shuffle()
    print "Dealing"
    # initial deal
    usercards = myDeck.deal(2)  # Puts 2 cards into the usercards list
    dealercards = myDeck.deal(2)  # Does the same thing for the dealer
    print "%s, your cards:" % (name)
    total = 0
    # tell the user what they got, including total
    for i in usercards:
        print "%s of %s" % (i[1], i[2])
        if i[0] > 10: 
            total += 10
        elif i[0] > 1:
            total += i[0]
        else:
            print "You got an Ace!"
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
    print "Your total is %d." % total

    keep_playing = True
    while ((total < 21) and (keep_playing)):
        keep_playing = raw_input("Would you like another card (y/N)? ")
        if (keep_playing != "") and (keep_playing[0].lower() == "y"):
            usercards += myDeck.deal(1)     # concatenates to user card list.
                                            # don't use append!
            # Tell them what they got, which is last usercards on list
            print "You got a %s of %s" % (usercards[-1][1], usercards[-1][2])
            # Calculate their total
            if usercards[-1][0] > 10: 
                total += 10
            elif usercards[-1][0] > 1:
                total += usercards[-1][0]
            else:
                print "You got an Ace!"
                if total + 11 <= 21:
                    total += 11
                else:
                    total += 1
            print "your total is",total
        else:
            keep_playing = False

    if total > 21:
        print "Oh, too bad! You busted!"
    elif total == 21:
        print "You got 21! You win!"
    else:
        print "You got %d. Now it's MY turn!" % (total)
    
    # Code for computer to play should be added here. It's basically the 
    #  same process, right? But it's going to make for a very long program...!

    print "Thanks for playing Blackjack, %s! See you in Vegas!" % (name)

if __name__ == "__main__":
    main()
