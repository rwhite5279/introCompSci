#!/usr/bin/env python
# One-Dimensional Life program

import random
import time

def createWorld():
    popSize = input("How many cells? ")
    world = []
    for i in range(popSize):
        world.append(random.randint(0,1))
    printWorld(world)
    return world

def countRadius(world,n,radius):
    # counts cells to either side of cell n
    count = 0
    for i in range(n-radius,n+radius+1):
        if i >= 0 and i < len(world):
            count += world[i] 
    return count

def printWorld(world):
    lineToPrint = ''
    for cell in world:
        if cell == 0: lineToPrint += '.'
        else: lineToPrint += '@'
    print lineToPrint

def evolve(world):
    # k = 2
    radius = 2
    # Set up rules as a dictionary
    rules = {5:0,4:1,3:0,2:1,1:0,0:0}
    while True:
        nextWorld = [0]*len(world)
        for i in range(len(world)):
            # print countRadius(world,i,radius)    
            nextWorld[i] = rules[countRadius(world,i,radius)]
        world = nextWorld[:]
        printWorld(world)
        time.sleep(0.1)
        # pause = raw_input()

def main():
    myWorld = createWorld()
    evolve(myWorld)

if __name__ == "__main__":
    main()
