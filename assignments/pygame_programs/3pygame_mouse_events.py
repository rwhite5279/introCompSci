#!/usr/bin/python
"""Mouse events trials"""

import pygame

x = y = 0
running = True
screen = pygame.display.set_mode((640,480))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print "mouse at (%d %d)" % event.pos
        
    screen.fill((0,0,0))
    pygame.display.flip()