#Name: Robert Mooy
#Instructor: Workman
#Project 3

from solverFuncs import *

puzzle = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
cages = get_cages()
checks = 0
backtracks = 0
row = 0
col = 0
print()
while row < 5:
     puzzle[row][col] +=1
     check_puzzle = check_valid(puzzle, cages)
     checks +=1
     if check_puzzle == True:
        col += 1
        if col >= 5:
            col = 0
            row += 1
     else: 
        while puzzle[row][col] == 5:
            backtracks += 1
            puzzle[row][col] = 0
            col -= 1
            if col < 0:
               col = 4
               row -= 1
   
print("---Solution---\n")
print("%d %d %d %d %d" % (puzzle[0][0], puzzle[0][1], puzzle[0][2], puzzle[0][3], puzzle[0][4]))
print("%d %d %d %d %d" % (puzzle[1][0], puzzle[1][1], puzzle[1][2], puzzle[1][3], puzzle[1][4]))
print("%d %d %d %d %d" % (puzzle[2][0], puzzle[2][1], puzzle[2][2], puzzle[2][3], puzzle[2][4]))
print("%d %d %d %d %d" % (puzzle[3][0], puzzle[3][1], puzzle[3][2], puzzle[3][3], puzzle[3][4]))
print("%d %d %d %d %d" % (puzzle[4][0], puzzle[4][1], puzzle[4][2], puzzle[4][3], puzzle[4][4])) 
print("\nchecks: %d backtracks: %d" % (checks, backtracks))
