def get_cages():
    numcages = int(input("Number of cages: "))
    cages = []
    x = 0
    for x in range(numcages):
       info = input("Cage number %d: " %x).split()
       new = []
       for i in info:
           new.append(int(i)) 
       cages.append(new)
    return cages

def check_row(row):
    seen = []
    for num in row:
       if num in seen and num != 0 or num > 5:
          return False
       else:
          seen.append(num)
    return True

def check_rows_valid(puzzle):
    for row in puzzle:
        if check_row(row) == False:
           return False 
    return True

def check_col(puzzle, index):
    seen = []
    for row in puzzle:
        if row[index] in seen and row[index] != 0 or row[index] > 5:
           return False
        else:
           seen.append(row[index])
    return True

def check_columns_valid(puzzle):
    index = 0
    for col in puzzle:
       if check_col(puzzle, index) == False:
          return False
       index += 1
    return True
 
def check_cage(puzzle, cage):
    cagesum = 0
    complete = True
    for index in cage[2:]:
       row = index // 5
       col = index % 5
       if puzzle[row][col] == 0:
          complete = False
       cagesum += puzzle[row][col]
    if cagesum != cage[0] and complete:
       return False
    if cagesum >= cage[0] and not complete:
       return False
    return True
    
def check_cages_valid(puzzle, cages):
    for cage in cages:
        if check_cage(puzzle, cage) == False:
           return False
    return True

def check_valid(puzzle, cages):
    if check_rows_valid(puzzle) == False:
       return False 
    elif check_columns_valid(puzzle) == False:
       return False
    elif check_cages_valid(puzzle, cages) == False:
       return False
    else:
       return True
