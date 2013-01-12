#!/usr/bin/python

"""Pong Demonstration, by Richard White, 2010-01-22

   THIS VERSION OF THE PROGRAM JUST SETS UP A SINGLE PADDLE
   
   This program is designed to demonstrate some of the more important 
   uses/functions/capabilities of Pygame, including
   * game clock
   * keyboard input
   * collision detection
   All, with comments galore! ;)
   
   A few notes about how I wrote this program: one step at a time:
   a) Get a screen to display.
   b) Get a paddle to show up.
   c) See if you can get the paddle to move.
   d) Put a "ball" on the screen.
   e) See if you can get the ball to move.
   f) See if you can recognize when the ball hits the paddle.
   g) Send the ball bouncing back across the screen appropriately.
   h) Get ball to bounce back towards you.
   i) Get a score counter to count when you miss it.
   j) etc...
   
   One step at a time! Use functions to organize your code!
   
"""

import pygame, sys
from pygame.locals import *   	# Useful for allowing us to use constant
								# variables like QUIT, K_ESCAPE, etc.

# Initialize Pygame and game clock
pygame.init()					# All Pygame programs have to start with this
main_clock = pygame.time.Clock()	# This object allows us to regulate how many
								# times a loop will iterate in one second.
								
# Initialize the Window
SCREEN_WIDTH = 800				# It's a convention to use capitals for
SCREEN_HEIGHT = 600				# identifiers that have a constant value
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Pong, by Richard White')

# Initialize colors for this game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize paddle
paddle_thickness = 20           # units are pixels
paddle_width = 100
paddle_position_y = (SCREEN_HEIGHT / 2) - (paddle_width / 2) # upper left y
paddle_position_x = SCREEN_WIDTH - paddle_thickness # upper left x
paddle = pygame.Rect(paddle_position_x, paddle_position_y, paddle_thickness, paddle_width)

# Initialize paddle and movement parameters
speed = 10                       # units are pixels. May be adjusted within game


# Main game loop
move_up = False
move_down = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:      # QUIT event is generated when user
                                    # closes a window
            pygame.quit()
            sys.exit()
        
        # Move paddle
        if event.type == KEYDOWN:
            if event.key == K_UP:
                move_up = True
                move_down = False
            if event.key == K_DOWN:
                move_down = True
                move_up = False
                
        if event.type == KEYUP:
            if event.key == K_ESCAPE or event.key == ord('q'):
                                # If user wants to quit
                 pygame.quit()
                 sys.exit()
            if event.key == K_UP:
                move_up = False
            if event.key == K_DOWN:
                move_down = False
        
    if move_up and paddle.top - speed > 0:
        paddle.top -= speed
    if move_down and paddle.bottom + speed < SCREEN_HEIGHT:
        paddle.top += speed
        
    screen.fill(BLACK)    
    pygame.draw.rect(screen,WHITE,paddle)
    pygame.display.update()
    main_clock.tick(400)
                
                
