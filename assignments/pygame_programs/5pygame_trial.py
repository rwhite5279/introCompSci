#!/usr/bin/python

import pygame
import random

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()  # This does what?
running = True

screen.fill((0,0,0)) # Prepare a screen color

while (running):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    screen.set_at((x,y),(red, green, blue))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()# Display screen
    clock.tick(10000)



