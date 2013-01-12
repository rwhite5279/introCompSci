"""randomWalker-whiter.py
Random Walker, by Richard White, 2011-02-28

A blindfolded person walks in random directions, and eventually (perhaps?) returns to his starting position. Model this situation using a pixel initially placed in the middle of a graphic screen.

For the RandomWalker, the simulation allows the walker to step in any direction. A random direction is generated as an angle off of the x-axis.

angle = random() * 2 * math.pi
# The new x and y positions are then given by these formulas:
x = x + cos(angle)
y = y + sin(angle) 

Not just any x and y values can be plotted, however-you can only plot integer values.

This program requires the pygame module to run, available from http://www.pygame.org  It can be easily modfified, however, to work with other graphics modules.
"""

import pygame # used for graphics capabilities
import sys # used to quit program when window is closed
import random # used to generate random direction
import math # used for pi function
from pygame.locals import *  # allows us to use machine-dependent features


#####################################################################
def initialize_walker():
    # set up pygame
    pygame.init()

    # set up window
    width = 400
    height = 300
    myScreen = pygame.display.set_mode((width, height), 0, 32)
    myFont = pygame.font.SysFont(None, 24)
    pygame.display.set_caption('Random Walker, by Richard White') # sets window title

    # identify some common colors
    WHITE = (255, 255, 255) # Red-Green-Blue color code
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    colors = [BLACK, RED, GREEN, WHITE]

    # Set up the game clock
    clock = pygame.time.Clock()

    # create screen background
    myScreen.fill(BLACK)  # fills screen with black

    # create step counter
    count = 0

    # place walker at middle of screen
    start_x = int(width / 2.0)
    start_y = int(height / 2.0)
    return width, height, myScreen, clock, count, colors, start_x, start_y, myFont

#####################################################################
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#####################################################################    
def move_walker(myScreen,x,y,colors,count,clock):
    angle = random.random() * 2 * math.pi # angle in rads is some fraction of 2*pi radians
    x = int(round(x + math.cos(angle)))
    y = int(round(y + math.sin(angle)))
    myScreen.set_at((x, y),(colors[1])) # displays a red pixel
    # print x, y For debugging purposes
    pygame.display.update()
    clock.tick(400)  # vary this number to get a balance between program responsiveness
                     # and CPU load on the machine
    myScreen.set_at((x,y),(colors[3]))  # converts old path to a white pixel
    count += 1
    return x, y, count

#####################################################################
def display_count(myScreen, count, height, myFont, colors):
    step_message = "Steps:" + str(count)
    myText = myFont.render(step_message, True, colors[3], colors[0])
    textRect = myText.get_rect()  # Place text on a rectangle surface, returns that surface (into textRect)
    textRect.left = 0
    textRect.bottom = height
    myScreen.blit(myText,textRect)            # puts text on screen

#####################################################################
def finished(myScreen, count, height, myFont, colors, clock):
    status = "The walker returned after " + str(count) + " steps!"
    status_text = myFont.render(status, True, colors[3], colors[0])
    textRect = status_text.get_rect()  # Place text on a rectangle surface, returns that surface (into textRect)
    textRect.left = 0
    textRect.bottom = height
    myScreen.blit(status_text,textRect)
    pygame.display.update()
    while 1:
        check_events()      # Wait until user closes window
        clock.tick(20)
    
#####################################################################
def main():
    width, height, myScreen, clock, count, colors, start_x, start_y, myFont = initialize_walker()
    x, y = start_x, start_y                 
    myScreen.set_at((start_x, start_y),(colors[2]))    # Center location is green
    returned = False
    while not returned:
        check_events()  # Check to see if the user has closed the windowd
        x,y,count = move_walker(myScreen,x,y,colors,count, clock)  # get a new position for the walker
        display_count(myScreen, count, height, myFont, colors)     # display the walker at the new position
        if x == start_x and y == start_y:                          # If we've returned, stop!
            returned = True
    finished(myScreen, count, height, myFont, colors, clock)       # Give final message
            
#####################################################################
if __name__ == "__main__":
    main()