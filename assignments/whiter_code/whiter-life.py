#!/usr/bin/env python
"""
Life Program, by Richard White, 2012-03-19
"""

import os
import random
import time

def printBoard(board,width,height):
    """prints the board every generation"""
    os.system("clear")
    for j in range(height):
        thisLine = ""
        for i in range(width):
            thisLine += board[i][j]
        print thisLine

def createBoard():
    """initializes a board"""
    board = []
    width = 160
    height = 55
    for i in range(width):
        board.append([])
        board[i] = []
        for j in range(height):
            board[i].append('.')
    return board,width,height

def fillBoard(board,width,height):
    """randomly fill board at beginning of simulation"""
    populationSize = 0.3 * height * width
    for cell in range(int(populationSize)):
        x = random.randrange(width)
        y = random.randrange(height)
        board[x][y] = "0"

def checkNeighbors(board,width,height,cellX,cellY):
    """count up all the neighbors in the 8 cells
    around a cell. Make sure you don't try to 
    count cells 'off the screen' that don't 
    exist in the array!"""
    cellCount = 0
    for i in range(cellX-1,cellX+2):
        for j in range(cellY-1, cellY+2):
            if (i == cellX) and (j == cellY):
                pass  # Don't count middle cell
            else:
                if (0 <= i < width) and (0 <= j < height):
                    if board[i][j] == "0":
                        cellCount += 1
    return cellCount

def evolve(board,width,height):
    nextGen,width,height = createBoard()
    for i in range(width):
        for j in range(height):
            count = checkNeighbors(board,width,height,i,j)
            """Now that we have the count, apply
            the rules for determining the status
            of this cell, and place the new cell
            state in the nextGen array."""
            if board[i][j] == "." and count == 3: 
                nextGen[i][j] = "0"
            elif board[i][j] == "0":
                if count < 2:
                    nextGen[i][j] = "."
                elif count > 3:
                    nextGen[i][j] = "."
                else:
                    nextGen[i][j] = "0"
    """Once we've gone through all cells, transfer
    nextGen board into board for iterating through
    next time."""
    
    """IMPORTANT NOTE:
    We need to transfer nextGen board to "board", but
    this statement won't work!
    board = nextGen[:][:]
    Can you see why? board is a variable local to evolve.
    We need to transfer nextGen out to the main program
    by returning it."""
    return nextGen


def main():
    board,width,height = createBoard()
    fillBoard(board,width,height)
    while True:
        printBoard(board,width,height)
        board = evolve(board,width,height)
        # time.sleep(0.8)
        # pause = raw_input()

if __name__ == "__main__":
    main()

