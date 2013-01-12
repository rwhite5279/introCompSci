#!/usr/bin/python
"""Mouse events trials"""

import pygame

bgcolor = 0,0,0
linecolor = 255,255,255
x = y = 0
running = True
screen = pygame.display.set_mode((640,480))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEMOTION:
        x,y = event.pos
        
    screen.fill(bgcolor)
    pygame.draw.line(screen,linecolor,(x,0),(x,479))
    pygame.draw.line(screen,linecolor,(0,y),(639,y))
    pygame.display.flip()