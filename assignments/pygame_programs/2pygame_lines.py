#!/usr/bin/python
"""pygame development, Richard White, 2011-02-19"""

import pygame

screen = pygame.display.set_mode((640,480))
running = True

while running:
    event = pygame.event.poll()  # poll grabs next event from the event queue
    if event.type == pygame.QUIT:
        running = False
        
    screen.fill((0,0,0))   # Make screen black
    pygame.draw.line(screen, (0,0,255), (0,0), (639,479))  # screen, color, start, end
    pygame.draw.aaline(screen,(0,255,0),(639,0), (0,479))  
    # lines above draw lines onto the buffer
    pygame.display.flip()  # Now display the buffer
    
    