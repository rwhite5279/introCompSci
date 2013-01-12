#!/usr/bin/python
"""Moving Lines example"""

import pygame

y = 0
x = 0
direction_y = 1
direction_x = 1
increment = 2
running = True
width = 800
height = 600
RED = (255,0,0)
WHITE = (0,0,0) 
screen = pygame.display.set_mode((width, height))
linecolor = RED
bgcolor = WHITE
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(bgcolor)
    pygame.draw.line(screen,linecolor,(0,y), (width-1, y))
    pygame.draw.line(screen,linecolor,(x,0),(x,height-1))
    
    y += direction_y * increment # increments 1
    x += direction_x * increment
    if y <= 0 or y >= height - 1:
        direction_y *= -1
    if x <= 0 or x >= width - 1:
        direction_x *= -1
    
    clock.tick(20)   # Makes program run 3 times slower, but uses much less CPU
    pygame.display.flip()
    
    
