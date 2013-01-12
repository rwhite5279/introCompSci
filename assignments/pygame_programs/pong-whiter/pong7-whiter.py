#!/usr/bin/python

"""Pong Demonstration, by Richard White, 2010-01-22

   INTRO SCREEN AT BEGINNING, and PRESS ANY KEY TO PLAY

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

import pygame, sys, random, time
from pygame.locals import *   	# Useful for allowing us to use constant
								# variables like QUIT, K_ESCAPE, etc.

######################## INITIALIZE FUNCTION #################################

def initialize():
    # Initialize Pygame and game clock
    pygame.init()					# All Pygame programs have to start with this
    main_clock = pygame.time.Clock()	# This object allows us to regulate how many
								# times a loop will iterate in one second.
    # Initialize the Window
    SCREEN_WIDTH = 800				# It's a convention to use capitals for
    SCREEN_HEIGHT = 600				# identifiers that have a constant value
    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    
    # Initialize colors for this game
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Initialize player scores
    left_score = 0
    right_score = 0
    
    # set up font - Here, we use default system font, size 48pt
    basicFont = pygame.font.SysFont(None, 60)
    smallFont = pygame.font.SysFont(None, 36)
    
    screen.fill(BLACK)    
    welcome_text = basicFont.render("Pong! by Richard White",True,WHITE,BLACK) # set up text
    welcome_textRect = welcome_text.get_rect()   # get_rect returns a rectangular shape containing
                                 # the surface, with parameters x, y, width, height
                                 # where x,y indicate upper-left corner
    welcome_textRect.centerx = screen.get_rect().centerx
    welcome_textRect.centery = screen.get_rect().centery
    screen.blit(welcome_text, welcome_textRect)   # place the text in the rectangle
    
    prompt_text = smallFont.render("A Python-based rendition of the classic arcade game. Left player uses 'w' and 's' to move the paddle up and down, and the right player uses 'up arrow' and 'down arrow' keys.", True, YELLOW, BLACK)
    prompt_textRect = prompt_text.get_rect()
    prompt_textRect = ((200,500),(600,550))
    screen.blit(prompt_text,prompt_textRect)

    pygame.display.update()  # nothing gets drawn on the screen until this is called!
    time.sleep(6)
    
    return pygame, main_clock, screen, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLUE, YELLOW, left_score, right_score, basicFont, smallFont
    
    # Note the boatload of variables that have to be returned? Object-oriented programming helps to fix a lot of this! :)

####################### RESET GAME ###############################################################

def reset_game(SCREEN_WIDTH, SCREEN_HEIGHT):
    """I had to add this function in, breaking it out from the Initialize function, because all of these variables needed to be reset everytime someone lost the game. Kind of a pain to have to write a new function at the very end of the programming process, but that's what we do! ;) """
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

    # Initialize the ball
    ball_thickness = 20
    ball_height = 20
    ball_position_y = (SCREEN_HEIGHT / 2) - (ball_height / 2)
    ball_position_x = (SCREEN_WIDTH / 2) - (ball_thickness / 2)
    ball = pygame.Rect(ball_position_x, ball_position_y, ball_thickness, ball_height)
    ball_direction_x = random.choice([-1,1])
    ball_direction_y = random.choice([-1,1])
    ball_speed_x = 5 * ball_direction_x
    ball_speed_y = 3 * ball_direction_y

    # Reset lost flag
    left_lost = right_lost = False
    
    return left_paddle, right_paddle, paddle_thickness, paddle_width, speed, ball, ball_thickness, ball_speed_x, ball_speed_y, left_move_up, left_move_down, right_move_up, right_move_down, left_lost, right_lost

###################### GET USER INPUT FUNCTION ###################################################

def analyze_keys(event, left_move_up, left_move_down, right_move_up, right_move_down):
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
            
    return left_move_up, left_move_down, right_move_up, right_move_down
    
###################### MOVE PADDLES FUNCTION ###########################################

def move_paddles(left_move_up, left_move_down, right_move_up, right_move_down, left_paddle, right_paddle, SCREEN_HEIGHT, speed):
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

    return left_paddle, right_paddle
    
###################### DETECT COLLISIONS FUNCTION ###########################################

def detect_collisions(ball, left_paddle, right_paddle, paddle_thickness, paddle_width, ball_thickness, ball_speed_x, ball_speed_y, SCREEN_WIDTH, SCREEN_HEIGHT, left_lost, right_lost):
    # Collision detection!!!
    # Two things that can happen:
    # a) the ball can collide with a paddle, in which case we need to reverse its x-direction, or 
    # b) the ball can hit the edge of the screen, in which case the paddle missed it
    # To hit the paddle, the middle of the ball has to hit within the width of the paddle

    # Check to see if we passed the edge of the paddle. If we do it once, the point is over
    if ball.left < 0 + paddle_thickness:
        if left_paddle.top < ball.top < left_paddle.bottom or \
            left_paddle.top < ball.bottom < left_paddle.bottom:
            ball_speed_x *= -1.1  # 1.1 factor means that the ball's speed increases with every hit!
            # Allow for spin
            if ball.top + ball_thickness / 2 < left_paddle.top + paddle_width:    
                ball_speed_y -= 2
            else:
                ball_speed_y += 2
        else:
            left_lost = True # point was lost

    if ball.left + ball_thickness > SCREEN_WIDTH - paddle_thickness:
        if right_paddle.top < ball.top < right_paddle.bottom or \
            right_paddle.top < ball.bottom < right_paddle.bottom:
            ball_speed_x *= -1.1
            if ball.top + ball_thickness / 2 < right_paddle.top + paddle_width:
                ball_speed_y -= 2
            else:
                ball_speed_y += 2
        else:
            right_lost = True # point was lost
    
    # Change direction if we hit the top or bottom of the screen  
    if (ball.top < 0) or (ball.bottom > SCREEN_HEIGHT):
        ball_speed_y *= -1
            
    return ball_speed_x, ball_speed_y, left_lost, right_lost
    
####################### DRAW SCREEN FUNCTION ###########################################

def draw_screen(screen, BLACK, WHITE, YELLOW, left_paddle, right_paddle, ball, left_score, right_score, basicFont, SCREEN_WIDTH, SCREEN_HEIGHT, main_clock):
    screen.fill(BLACK)    
    pygame.draw.rect(screen,WHITE,right_paddle)
    pygame.draw.rect(screen,WHITE,left_paddle)
    pygame.draw.rect(screen,YELLOW,ball)
    
    left_text = basicFont.render(str(left_score),True,WHITE,BLACK) # set up text
    left_textRect = left_text.get_rect()   # get_rect returns a rectangular shape containing
                                 # the surface, with parameters x, y, width, height
                                 # where x,y indicate upper-left corner
    left_textRect.centerx = SCREEN_WIDTH / 4  # 
    left_textRect.centery = SCREEN_HEIGHT - 30
    screen.blit(left_text, left_textRect)   # place the text in the rectangle
    
    right_text = basicFont.render(str(right_score),True,WHITE,BLACK) # set up text
    right_textRect = right_text.get_rect()   # get_rect returns a rectangular shape containing
                                 # the surface, with parameters x, y, width, height
                                 # where x,y indicate upper-left corner
    right_textRect.centerx = SCREEN_WIDTH * 3 / 4  # 
    right_textRect.centery = SCREEN_HEIGHT - 30
    screen.blit(right_text, right_textRect)   # place the text in the rectangle
    
    pygame.display.update()  # nothing gets drawn on the screen until this is called!
    main_clock.tick(400)


###################### MAIN PROGRAM ####################################################

def main():
    # initialize everything
    pygame, main_clock, screen, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLUE, YELLOW, left_score, right_score, basicFont, smallFont = initialize()
    
    while left_score < 7 and right_score < 7:
        # reset the game
        
        screen.fill(BLACK)    
        welcome_text = basicFont.render("Press <Enter> to continue...",True,WHITE,BLACK) # set up text
        welcome_textRect = welcome_text.get_rect()   # get_rect returns a rectangular shape containing
                                     # the surface, with parameters x, y, width, height
                                     # where x,y indicate upper-left corner
        welcome_textRect.centerx = screen.get_rect().centerx
        welcome_textRect.centery = screen.get_rect().centery
        screen.blit(welcome_text, welcome_textRect)   # place the text in the rectangle

        pygame.display.update()  # nothing gets drawn on the screen until this is called!
        # keypress to continue
        time.sleep(3)
            
        left_paddle, right_paddle, paddle_thickness, paddle_width, speed, ball, ball_thickness, ball_speed_x, ball_speed_y, left_move_up, left_move_down, right_move_up, right_move_down, left_lost, right_lost = reset_game(SCREEN_WIDTH, SCREEN_HEIGHT)                
        while not (left_lost or right_lost):         # This is the "game loop,' which we'll be constantly running
            for event in pygame.event.get():
                if event.type == QUIT:      # QUIT event is generated when user closes a window
                    pygame.quit()
                    sys.exit() 
                # See if they entered anything, and bring results back here           
                left_move_up, left_move_down, right_move_up, right_move_down = analyze_keys(event, left_move_up, left_move_down, right_move_up, right_move_down)
            # move paddles, if keys have been pressed      
            left_paddle, right_paddle = move_paddles(left_move_up, left_move_down, right_move_up, right_move_down, left_paddle, right_paddle, SCREEN_HEIGHT, speed)
            # Move the ball
            ball.left += ball_speed_x
            ball.top += ball_speed_y
            # Detect collisions
            ball_speed_x, ball_speed_y, left_lost, right_lost = detect_collisions(ball, left_paddle, right_paddle, paddle_thickness, paddle_width, ball_thickness, ball_speed_x, ball_speed_y, SCREEN_WIDTH, SCREEN_HEIGHT, left_lost, right_lost) 
            # Draw screen
            # See if anyone lost
            if left_lost:
                right_score += 1
                break
            if right_lost:
                left_score +=1
                break
            draw_screen(screen, BLACK, WHITE, YELLOW, left_paddle, right_paddle, ball, left_score, right_score, basicFont, SCREEN_WIDTH, SCREEN_HEIGHT, main_clock)
        
              
if __name__ == "__main__":
    main()              
