# a Mancala game in python
# by: Keshav Barker
# 2023-8-10
# version 1.0
# TODO: add a GUI

import random
import time
import sys
import os
import copy

# global variables

# the board is a list of lists

# the first board is the starting board
# the second board is the current board
StartingBoard = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]    # the starting board
Board = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]            # the current board

# the first list is the player's score
# the second list is the computer's score
score = [0, 0]                                      # the score
# the first list is the player's turn
# the second list is the computer's turn
turn = [True, False]                                # whose turn it is
# the first list is the player's name
# the second list is the computer's name
name = ["Player", "Computer"]                       # the player's name
# the first list is the player's side
# the second list is the computer's side
side = ["top", "bottom"]                            # the player's side
# the first list is the player's move
# the second list is the computer's move
move = [0, 0]                                       # the first item is player move, the second item is computer move

# initialize the board
def initBoard():
    global Board
    Board = copy.deepcopy(StartingBoard)        # copy the starting board to the current board

# print the board
def printBoard():
    global Board
    print(" 1  2  3  4  5  6")              # print the column numbers
    print("  ---------------------")          # print the top border
    for i in range(2):
        print("|")                         # for each row
        for j in range(6):                     # for each column
            print("|", end="")                 # print the side border
            print(Board[i][j], end=" ")       # print the number of stones in the pit    
        print(side[i], end=" ")               # print the side
        print("|")                             # print the side border
    print("  ---------------------")          # print the bottom border
    print(" 1  2  3  4  5  6")              # print the column numbers

# print the score
def printScore():
    global score
    print("Score:")                            # print the score
    print(name[0], score[0])                   # print the player's score
    print(name[1], score[1])                   # print the computer's score

# print the turn
def printTurn():
    global turn
    print(name[0], turn[0])                    # print the player's turn
    print(name[1], turn[1])                    # print the computer's turn

# print the move
def printMove():
    global move
    print(name[0], move[0])                    # print the player's move
    print(name[1], move[1])                    # print the computer's move

# print the side
def printSide():
    global side
    print(name[0], side[0])                    # print the player's side
    print(name[1], side[1])                    # print the computer's side

# print the board, score, turn, move, and side
def printAll():
    printBoard()                               # print the board
    printScore()                               # print the score
    printTurn()                                # print the turn
    printMove()                                # print the move
    printSide()                                # print the side

# check if the game is over
def gameOver():    # check if either side of the board is empty
    # check if either side of the board is empty
    if sum(Board[0]) == 0 or sum(Board[1]) == 0:
        return True
    else:
        return False

# check if the player's move is valid
def validMove():
    global move
    global side
    global Board
    if side[0] == "top":                        # if the player's side is the top
        if Board[0][move[0] - 1] == 0:          # if the player's move is invalid
            return False
        else:                                   # if the player's move is valid
            return True
    else:                                       # if the player's side is the bottom
        if Board[1][move[0] - 1] == 0:          # if the player's move is invalid
            return False
        else:                                   # if the player's move is valid
            return True

# make the player's move
# return True if the player gets another turn
# return False if the player does not get another turn
# return None if the player's move is invalid
def makeMove():   # code for making the move goes here
    global move
    global Board
    global score
    global turn
    global side
    
    if validMove(): # if the player's move is valid
        stones = Board[0][move[0] - 1] # get the number of stones in the selected pit
        Board[0][move[0] - 1] = 0 # empty the selected pit
        i = move[0] # start at the selected pit
        while stones > 0: # while there are still stones to distribute
            i += 1 # move to the next pit
            if i == 6: # if we reach the end of the player's side
                if side[0] == "top": # if the player's side is the top
                    score[0] += 1 # add a point to the player's score
                else: # if the player's side is the bottom
                    Board[1][0] += 1 # add a stone to the computer's pit
                stones -= 1 # remove a stone from the player's pit
            elif i > 6: # if we reach the computer's side
                i = 0 # start at the beginning of the player's side
            else: # if we are still on the player's side
                Board[0][i] += 1 # add a stone to the current pit
                stones -= 1 # remove a stone from the player's pit
        if i == 6: # if the last stone landed in the player's mancala
            return True # the player gets another turn
        elif Board[0][i] == 1 and i < 6: # if the last stone landed in an empty pit on the player's side
            score[0] += Board[1][5 - i] + 1 # add the stones in the opposite pit and the last stone to the player's score
            Board[0][i] = 0 # empty the current pit
            Board[1][5 - i] = 0 # empty the opposite pit
            return True # the player gets another turn
        else: # if the last stone landed in a non-empty pit on the player's side
            turn = [False, True] # it is now the computer's turn
            side = ["bottom", "top"] # the computer is now on the bottom
            move[1] = random.randint(1, 6) # choose a random move for the computer
            return False # the player does not get another turn
    else:
        return None

# make the computer's move
# return True if the computer gets another turn
# return False if the computer does not get another turn
def makeComputerMove():   # code for making the computer's move goes here
    global move
    global Board
    global score
    global turn
    global side
    
    if validMove(): # if the computer's move is valid
        stones = Board[1][move[1] - 1] # get the number of stones in the selected pit
        Board[1][move[1] - 1] = 0 # empty the selected pit
        i = move[1] # start at the selected pit
        while stones > 0: # while there are still stones to distribute
            i += 1 # move to the next pit
            if i == 6: # if we reach the end of the computer's side
                if side[1] == "top": # if the computer's side is the top
                    Board[0][0] += 1 # add a stone to the player's pit
                else: # if the computer's side is the bottom
                    score[1] += 1 # add a point to the computer's score
                stones -= 1 # remove a stone from the computer's pit
            elif i > 6: # if we reach the player's side
                i = 0 # start at the beginning of the computer's side
            else: # if we are still on the computer's side
                Board[1][i] += 1 # add a stone to the current pit
                stones -= 1 # remove a stone from the computer's pit
        if i == 6: # if the last stone landed in the computer's mancala
            return True # the computer gets another turn
        elif Board[1][i] == 1 and i < 6: # if the last stone landed in an empty pit on the computer's side
            score[1] += Board[0][5 - i] + 1 # add the stones in the opposite pit and the last stone to the computer's score
            Board[1][i] = 0 # empty the current pit
            Board[0][5 - i] = 0 # empty the opposite pit
            return True # the computer gets another turn
        else: # if the last stone landed in a non-empty pit on the computer's side
            turn = [True, False] # it is now the player's turn
            side = ["top", "bottom"] # the player is now on the top
            move[0] = int(input("Enter your move: ")) # get the player's move
            return False # the computer does not get another turn
    else: # if the computer's move is invalid
        return None
    
# play the game
def playGame():
    global move
    global Board
    global score
    global turn
    global side
    
    initBoard() # initialize the board
    printAll() # print the board, score, turn, move, and side
    while not gameOver(): # while the game is not over
        if turn[0]: # if it is the player's turn
            move[0] = int(input("Enter your move: ")) # get the player's move
            while not validMove(): # while the player's move is invalid
                print("Invalid move!") # print an error message
                move[0] = int(input("Enter your move: ")) # get the player's move
            if makeMove(): # if the player gets another turn
                print("You get another turn!") # print a message
            printAll() # print the board, score, turn, move, and side
        else: # if it is the computer's turn
            move[1] = random.randint(1, 6) # choose a random move for the computer
            while not validMove(): # while the computer's move is invalid
                move[1] = random.randint(1, 6) # choose a random move for the computer
            if makeComputerMove(): # if the computer gets another turn
                print("The computer gets another turn!") # print a message
            printAll() # print the board, score, turn, move, and side
    if score[0] > score[1]: # if the player won
        print("You won!") # print a message
    elif score[0] < score[1]: # if the computer won
        print("The computer won!") # print a message
    else: # if it is a tie
        print("It's a tie!") # print a message

# main function
def main():
    playGame() # play the game

# run the main function
if __name__ == "__main__":
    main()

# end of file
