"""
"A one-dimensional cellular automaton (hereafter called a line automoton) consists of an infinite strip of cells changing states according to a given set of rules. As in the game of Life a cosmic clock ticks away and at each tick every cell enters a state determined by its previous state and the previous states of cells in its neighborhood. A line automaton is specificed by giving two numbers called k and r as well as a set of rules for deriving the next state of a cell. The first number, k, determines how many states are allowed for each cell. In Life there are just two states and so k is equal to 2; among the line automata to be consdered, higher values of k are common. The secon number, r, referes to the radius of neighborhoods use to compute the next state of a cell. The present state of a cell and the states of its r neighboors on both sides determine the next state of the cell. For example, if r is equal to 2 and k is equal to 3, a certain rule might specify that when a cell's neighborhood looks like [0,2,1,1,0] the next state occupied by the central cell would be [3].

The set of rules that define a line automaton must decided the fate of a cell for every possible configuration of states inhabiting its neighborhood. Depending on the size of k and r the number of possible rule sets to consider can be enormous... The number of possible rule sets to consider is greatly reduced by adopting the ones Wolfram calls totalistic. Here the next state of a given cell is determined only by the sum of the states in the cell's neighborhood. The sum includes the state of the given cell. The number of possible sums varies from 0 to m, where m is the largest value of the state multiplied by the size of the neighborhood. If one specifies how these sums become the central cell's next state, one has specified the line automaton completely.

For example, there is a very interesting line automaton governed by totalistic rules given in this table:
           +-----------------------+
       sum | 5 | 4 | 3 | 2 | 1 | 0 |
           +-----------------------+
next state | 0 | 1 | 0 | 1 | 0 | 0 |
           +-----------------------+
"

Write a program to track a line automaton.

"""







































"""
PSEUDOCODE

1. Create the initial state (randomly?) as a list of digits
2. Display the list
2. Create a function with the "rules" hard-coded into it
3. Run through the list one item at a time, and survey each item; use the rule table to determine the next state of that element.
4. Display the list
5. Repeat

"""




















































"""
MORE SPECIFIC PSEUDOCODE

#identify number of cells in line

# set up a list for the cells, and

# maybe set up another list for the "future cells" that we'll be plugging new cell values into

# define rules in the table so that we can get future cell state, depending on population count
           +-----------------------+
       sum | 5 | 4 | 3 | 2 | 1 | 0 |
           +-----------------------+
next state | 0 | 1 | 0 | 1 | 0 | 0 |
           +-----------------------+
# m = 5,4,3,2,1,0; ? = 0,1,0,1,0,0
rules = [0,0,1,0,1,0]
# thus rules[population_sum] will give the value of the next generation of cell

# We've set everything up... now it's time to see what happens!
# Go through each cell, and total the values for neighbors

# Use this total to determine the value of the futurecell by looking at that table (the list)

# After filling up newcells list, copy it into cells so that we can start the whole process again

"""
































































"""
This version of the program below is a little more full-featured than the psuedocode above would suggest. In this version, the radius can be specified via "radius", and the number of cells in the line can be specified via "numcells". 
"""

import random
import time

def print_cells(cells):
    line = ''
    for a_cell in cells:
        if a_cell == 1: line += '0'
        else: line += '.'
    print line
    time.sleep(0.01)
    
numcells = 160
cells = []
nextcells = []
# define rules, where
# m = 5,4,3,2,1,0; ? = 0,1,0,1,0,0
k = 2  # This value isn't currently used, but represents the binary cell state
radius = 3  # This value represents the radius checked on either side of the current cell
rules = [0,0,0,1,1,0,1,0]
# thus rules[population_sum] will give the value of the next generation of cell
# fill up cell list
for i in range(numcells):
    cells.append(random.choice([0,1]))
    nextcells.append(0)   # fill this up for future use
print_cells(cells)
# We've set everything up... now it's time to see what happens!
while 1:
    fullpopulation = 0
    for i in range(radius,numcells-radius):   # smaller list so that we can get full addition
        local_population_sum = 0
        for j in range(i-radius, i+radius+1):
            local_population_sum += cells[j]
        nextcells[i] = rules[local_population_sum]
        fullpopulation += cells[i]   # keep track of total population for this generation
    # After going through, put future cells into cells
    cells[:] = nextcells
    print_cells(cells)
    if fullpopulation == 0: break
    
