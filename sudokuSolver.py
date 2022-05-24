import sys
sys.setrecursionlimit(5000)

board = [[0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 0, 3], [0, 7, 4, 0, 8, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 0, 0, 2], [0, 8, 0, 0, 4, 0, 0, 1, 0], [6, 0, 0, 5, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 7, 8, 0], [5, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 0]]

def print_board(board):
    #printing 2d array board
    #print("Your board:")
    for r in board:
        for c in r:
           print(c, end = " ")
        print()

#finds current index, iterates through 0 locations
def currIndex(board, index):
    currRow = 0
    for r in board:
        currCol = 0
        for c in r:
            if(c == 0):
                index[0] = currRow
                index[1] = currCol
                return True
            currCol += 1
        currRow += 1

def solvable(board):
    #board[4][8] = 8
    #print_board(board)
    #val = valid_col(board, 1)
    #val = valid_box(board, 4, 8)
    #print(val)
    index = [0, 0]
    if(not currIndex(board, index)):
        return True
    
    row = index[0]
    col = index[1]

    for val in range(1,10):
        if(check_location(board, row, col, val)):
            board[row][col] = val
            if(solvable(board)):
                return True
            board[row][col] = 0

    return False
    
#check if column is valid for given input
def valid_col(board, colNum, val):
    N = 9
    arr = [0]*N
    for row in board:
        i = 0
        for col in row:
            if(i == colNum and col != 0):
                if(arr[col-1] == 1 or col == val):
                    return False
                else:
                    arr[col-1] = 1
            i+=1
    return True

#check if row is valid for given input
def valid_row(board, rowNum, val):
    N = 9
    arr = [0]*N
    i = 0
    for row in board:
        if(i == rowNum):
            for col in row:
                if(col != 0):
                    if(arr[col-1] == 1 or col == val):
                        return False
                    else:
                        arr[col-1] = 1
        i+=1
    return True

#check if 3x3 box is valid for given input
def valid_box(board, rowNum, colNum, val):
    rowUp = 2
    rowDown = 0
    colUp = 2
    colDown = 0
    if(rowNum > 2 and rowNum <=5):
        rowUp = 5
        rowDown = 3
    if(rowNum > 5 and rowNum <=8):
        rowUp = 8
        rowDown = 6
    if(colNum > 2 and colNum <=5):
        colUp = 5
        colDown = 3
    if(colNum > 5 and colNum <=8):
        colUp = 8
        colDown = 6
    
    N = 9
    arr = [0]*N
    r = 0
    for row in board:
        if(r <= rowUp and r >= rowDown):
            c = 0
            for col in row:
                if(c <= colUp and c >= colDown):
                    if(col != 0):
                        if(arr[col-1] == 1 or col == val):
                            return False
                        else:
                            arr[col-1] = 1
                c+=1
        r+=1
    return True

def check_location(board, row, col, val):
    #board[row][col] = val
    #print_board(board)
    bool1 = valid_col(board, col, val)
    bool2 = valid_row(board, row, val)
    bool3 = valid_box(board, row, col, val)
    if(bool1 == True and bool2 == True and bool3 == True):
        return True
    return False

print("Your board:")
print_board(board)
val = solvable(board)
print(val)
print("Solved board:")
print_board(board)
