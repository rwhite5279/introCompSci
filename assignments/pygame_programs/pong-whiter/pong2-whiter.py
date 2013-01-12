#!/usr/bin/python

"""Pong Demonstration, by Richard White, 2010-01-22

   THIS VERSION OF THE PROGRAM ADDS A SECOND PADDLE
   
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

# Initialize paddles
paddle_thickness = 20           # units are pixels
paddle_width = 100
right_paddle_position_y = (SCREEN_HEIGHT / 2) - (paddle_width / 2) # upper left y
right_paddle_position_x = SCREEN_WIDTH - paddle_thickness # upper left x
right_paddle = pygame.Rect(right_paddle_position_x, right_paddle_position_y, paddle_thickness, paddle_width)
left_paddle_position_y = (SCREEN_HEIGHT / 2) - (paddle_width / 2) # upper left y
left_paddle_position_x = 0 # upper left x
left_paddle = pygame.Rect(left_paddle_position_x, left_paddle_position_y, paddle_thickness, paddle_width)

# Initialize paddle and movement parameters
speed = 10                       # units are pixels. May be adjusted within game

# Initialize all movement to False, at least until they push a button
right_move_up = False
right_move_down = False
left_move_up = False
left_move_down = False

while True:         # This is the "game loop,' which we'll be constantly running
    for event in pygame.event.get():
        if event.type == QUIT:      # QUIT event is generated when user
                                    # closes a window
            pygame.quit()
            sys.exit()
                    
        if event.type == KEYDOWN:  # If a key has been pressed down
            # Move paddle for right user
            if event.key == K_UP:  # Examines up "up arrow" key
                right_move_up = True
                right_move_down = False
            if event.key == K_DOWN:  # Examines the "down arrow" key
                right_move_down = True
                right_move_up = False
            # Move paddle for left user
            if event.key == ord('w'):  # Examines the "w" key
                left_move_up = True
                left_move_down = False
            if event.key == ord('s'):   # Examines the "s" key
                left_move_down = True
                left_move_up = False
            
        if event.type == KEYUP:   # If a key has been released
            if event.key == K_ESCAPE or event.key == ord('q'):
                # If user wants to quit
                pygame.quit()
                sys.exit()
            if event.key == K_UP:
                right_move_up = False
            if event.key == K_DOWN:
                right_move_down = False
            if event.key == ord('w'):
                left_move_up = False
            if event.key == ord('s'):
                left_move_down = False
           
    # Now, let's actually change the paddles location if they've done something.       
    if right_move_up: 
        right_paddle.top -= speed
    elif right_move_down:
        right_paddle.top += speed
    if right_paddle.top < 0:
        right_paddle.top = 0
    if right_paddle.bottom > SCREEN_HEIGHT:
        right_paddle.bottom = SCREEN_HEIGHT
        
    if left_move_up: 
        left_paddle.top -= speed
    elif left_move_down:
        left_paddle.top += speed
    if left_paddle.top < 0:
        left_paddle.top = 0
    if left_paddle.bottom > SCREEN_HEIGHT:
        left_paddle.bottom = SCREEN_HEIGHT
    
    screen.fill(BLACK)    
    pygame.draw.rect(screen,WHITE,right_paddle)
    pygame.draw.rect(screen,WHITE,left_paddle)
    pygame.display.update()  # nothing gets drawn on the screen until this is called!
    main_clock.tick(400)
                
                