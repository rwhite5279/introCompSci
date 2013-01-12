"""Life Program, by Richard White, 2011-03-04
Conway's Game of Life is a cellular automoton devised by John H. Conway in 1970. A two-dimensional orthogonal grid of cells is populated with single-celled organisms, which may or may not survive in the future based on a simple set of 4 rules:
1. A live cell with < 2 neighbors dies, due to underpopulation.
2. A live cell with 2-3 neighbors lives in to the next generation.
3. A live cell with > 3 neighbors dies, due to overpopulation.
4. An empty cell with 3 neighbors becomes a live cell, due to reproduction.

More information about Conway's Game of Life may be found online at http://en.wikipedia.org/wiki/Conway's_Game_of_Life
"""

import random   # Used to generate initial board
import os       # Used to clear the screen
import time     # Used to slow down motion on the board to a reasonable rate
import copy     # Used to copy new generation's board to old board
# import pygame   # Used to display graphic version of board, when implemented

####################################################################################    
def initialize_game():
    """This function establishes the width and height of the board, and fills it with 0s. It then goes through and places some 1s randomly in a center section of the board."""
    WIDTH, HEIGHT = 150, 60
    # WIDTH, HEIGHT = 60, 20
    generation = 0
    board = []
    for i in range(WIDTH):
        column = []
        for j in range(HEIGHT):
            column.append(".")  
        board.append(column)
    for i in range(int(0.2*WIDTH), int(0.8*WIDTH)):
        for j in range (int(0.2*HEIGHT), int(0.8*HEIGHT)):
            board[i][j] = random.choice([".","0"])
    return WIDTH, HEIGHT, board, generation

####################################################################################
def initialize_graphics():
    """We'll be working on a computer graphics version of this program a little later. For now, I just want to make sure that I get the logic right in this game."""
    pass   

####################################################################################
def count_neighbors(i,j,board):
    """This function counts up the neighbors around a given cell."""
    count = 0
    for y in range(j-1, j+2):
        for x in range(i-1, i+2):
            # print "x, y, board[x][y] are", x, y, board[x][y]
            if x == i and y == j:
                pass
            elif board[x][y] == "0":
                count += 1
                # print "We counted it"
    # print "Count of",i,j,"is",count
    return count

####################################################################################    
def live_or_die(WIDTH, HEIGHT, board, generation):
    """One of the challenges of this program is that you can't change cells one-by-one: we'll alter the state of the board prematurely. We need to do our accounting of each cell's status, create a next_generation board that includes everything, and then transfer that to the main board."""
    # Initialize next_board to nothing
    next_board = []
    for i in range(WIDTH):
        column = []
        for j in range(HEIGHT):
            column.append(".")
        next_board.append(column)
    # Now go through and collect states of next generation cells based on current generation
    for i in range(1, WIDTH - 1):  # Don't go through entire board, because we have to check border cells in our accounting
        for j in range(1, HEIGHT - 1):
            # Apply Conways rules here:
            count = count_neighbors(i,j,board)
            if board[i][j] == "0":   # if the cell is alive
                if count < 2 or count > 3:
                    next_board[i][j] = "."
                else:
                    next_board[i][j] = "0"
            if board[i][j] == ".":
                if count == 3:
                    next_board[i][j] = "0"
                else:
                    next_board[i][j] = "."
    # Finally, copy next_board into board
    board = copy.deepcopy(next_board)  # Have to use the copy function to get a new copy!
    generation += 1
    return board, generation
    
####################################################################################                
def print_board(WIDTH, HEIGHT, board, generation):
    os.system("clear")  # clears the screen out so we can start printing at the top
    print "John Conway's Game of Life"
    for j in range(HEIGHT):
        row = ""
        for i in range(WIDTH):
            row = row + board[i][j]
        print row
    print "Generation:",generation
        
####################################################################################                
def test_board():
    """This board was used during debugging, but is not part of the regular distribution. This function has been left here to aid in future debugging efforts when the graphics version of the program gets implemented."""
    WIDTH = 6
    HEIGHT = 4
    board = [[".",".","0","0"],["0",".",".","."],["0","0","0","."],["0","0","0","0"],["0","0","0","."],["0","0","0","."]]
    print board
    print board [5][3]
    return WIDTH, HEIGHT, board

####################################################################################                    
def main():
    width, height, board, generation = initialize_game()
    while 1:
        print_board(width, height, board, generation)
        board, generation = live_or_die(width, height, board, generation)
        # time.sleep(0.5)  # Wait for 0.5 seconds
        # wait = raw_input("[Enter] to continue..."   # Also used for debugging purposes

####################################################################################                
if __name__ == "__main__":
    main()