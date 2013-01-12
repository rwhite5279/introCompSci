#!/usr/bin/python

"""
party.py, by Richard White, 2011-05-04

This program is a simulation that tries to model a party taking place in a room. Party attendees show up at the door of the room, one by one, and display certain behaviors in interacting with the room and the other people in it.

This program uses curses to draw the room and move the characters about in it. It uses a 2-dimensional "list of lists" to track the people and objects in the room, and uses an object of the class Person for each party guest. Individual types of party guests are specified in further detail below.

Information on using "curses" to control display is available online at
http://docs.python.org/howto/curses.html#curses-howto
and at
http://heather.cs.ucdavis.edu/~matloff/Python/PyCurses.pdf
"""

import curses
import traceback
import time
import random

# -----------------------------------------------------------------------------
def init_screen():
    """This is a standard initialization function for curses, setting up the screen"""
    stdscr = curses.initscr()   # returns a window object representing the screen
    curses.noecho()             # turns off auto echo of key input
    curses.cbreak()             # allows computer to process key without [Enter]
    stdscr.keypad(1)            # enables keypad mode
    curses.start_color()
    return stdscr

# -----------------------------------------------------------------------------

def restore_screen(stdcr):
    """Standard shutdown function that returns screen to its original state before quitting the program."""
    curses.nocbreak();
    curses.echo()               # reverses terminal settings
    curses.endwin()             # restores terminal
    stdscr.keypad(0)

# -----------------------------------------------------------------------------

def init_room():
    """This sets up the initial room in an x-y grid. Each location is indicated by a '.', with additional special characters for other features in the room: '0' are walls, '%' are tables, '>' represents a speaker (music)..."""
    room=[]
    width = 40
    height = 15
    # Set up room in general
    for x in range(width):
        room.append([])   # initalize list for room column y
        for y in range(height):
            room[x].append('.')
    # Set up walls
    for x in range(width):
        room[x][0] = '*'
        room[x][height-1] = '*'
    for y in range(height):
        room[0][y] = "*"
        room[width-1][y] = "*"
    # Set up refreshments table
    for x in range(7, 13):
        for y in range(height - 6, height - 3):
            room[x][y] = "%"
    # Set up door
    room[0][3] = "/"
    return room

# -----------------------------------------------------------------------------
            
def print_room(room, myParty, stdscr):
    for x in range(len(room)):
        for y in range(len(room[x])):
            stdscr.addch(y,x,room[x][y])
    stdscr.addstr(16,0,"Status: " )
    myParty.view()
    stdscr.refresh()    # Draw screen
        
# -----------------------------------------------------------------------------

class Person:
    """The Person class has attributes Location (x,y), Satisfaction (sliding scale, very satisfied - not satisfied), Inebriation (sliding scale, sober - drunk), Socialness (very sociable - not sociable), Gender (Male, Female), Orientation (Straight, Gay, Bi), Independence (Independent - Dependent)."""
    
    def __init__(self,location, comfortlevel, socialness):
        """location is a two-item list containing x, y coordinates"""
        self.location = location
        self.comfortlevel = comfortlevel
        self.socialness = socialness
        
    def get_location(self):
        return self.location
        
    def get_comfortlevel(self):
        return self.comfortlevel
        
    def get_socialness(self):
        return self.socialness
        
    def move(self,delta):
        self.location = [ self.location[0] + delta[0] , self.location[1] + delta[1]]
        
    def show(self):
        locationstring = str(self.location[0])+","+str(self.location[1])+"; "
        reportstring = locationstring + str(self.comfortlevel) + " " + str(self.socialness)
        return reportstring

# -----------------------------------------------------------------------------

class Party:
    """The Party class contains all of the Guests, ie. all the Persons in the room."""
    def __init__(self):
        self.people = []

    def add_guest(self,guest):
        self.people.append(guest)

    def size(self):
        return len(self.people)
        
    def view(self):
        for person in self.people:
            stdscr.addstr(17 + self.people.index(person) , 0, person.show())

    def step(self,self.people):
        for person in self.people:
	    self.people.move()

# -----------------------------------------------------------------------------

        guest.move[1,0]
def increase_comfort(room,myParty,guest):
    """This function checks the guest in relation to everyone else at the party, and attempts to determine whether or not they should move, and in which direction. Things to check for are the walls, the table, the door, other people (depending on their qualities)..."""
    pass

# -----------------------------------------------------------------------------

def watch(stdscr,myParty,room):
    """Each time through the loop, we will 1. Randomly have a person show up at the door, and 2. Cycle through all the people in the room and allow them to move based on their comfort level."""
    # Everyone currently in room moves
    myParty.step()     # iterate and have everyone move 
    # See if anyone new has shown up
    person_showing_up = False
    if random.randrange(5) == 0: person_showing_up = True
    if person_showing_up:
        guest_number = myParty.size() + 1
        # Place new person at room[1][3] (just in from door)
        new_guy = Person([1,3],3,8) # New person, low comfort, high social
        room[1][3] = "S"  # Socialite
        myParty.add_guest(new_guy)   # Add this guy to the Party object
      

# -----------------------------------------------------------------------------  

if __name__ == '__main__':
    try:
        stdscr = init_screen()
        room = init_room()
        myParty = Party()
        while 1:
            print_room(room, myParty, stdscr)
            watch(stdscr,myParty,room)
            stdscr.getstr(0,0)  # Waits for user to enter a str (pausing program)
        restore_screen(stdscr)
    except:
        restore_screen(stdscr)
        traceback.print_exc()
   
