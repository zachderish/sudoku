from tkinter import *
from sudokuSolver import check_location, solvable, print_board

root = Tk()
root.title("Sudoku")

board1 = [[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], 
[8, 2, 0, 1, 0, 0, 0, 4, 0], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], 
[0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]

board3 = [[0, 2, 0, 6, 0, 8, 0, 0, 0], [5, 8, 0, 0, 0, 9, 7, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0, 0], 
[3, 7, 0, 0, 0, 0, 5, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 8, 0, 0, 0, 0, 1, 3], 
[0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 9, 8, 0, 0, 0, 3, 6], [0, 0, 0, 3, 0, 6, 0, 9, 0]]

board5 = [[0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 0, 3], [0, 7, 4, 0, 8, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 0, 0, 2], [0, 8, 0, 0, 4, 0, 0, 1, 0], [6, 0, 0, 5, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 7, 8, 0], [5, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 0]]

e = Entry(root, width = 50)
e.pack()

#opening sudoku window
def sudokuButton():
    easyButton.grid(row=1,column=0)
    intButton.grid(row=1,column=1)
    hardButton.grid(row=1,column=2)

#create board to use when checking inputs
newBoard = [[0 for r in range(9)] for c in range(9)]
#not currently in use
solvedBoard = [[0 for r in range(9)] for c in range(9)]
#list for labels and entries
entriesLabels = list()

#checks inputs
def checkClick():
    counter = 0
    #loads values from entriesLabels to newBoard
    for i in entriesLabels:
        value = 0
        #add blank values as 0 in newBoard
        try:
            value = i.get()
            if(len(value) == 0):
                value = 0
        except:
            value = i
        newBoard[int(counter/9)][counter%9] = int(value)
        counter+=1
    #delete old label to update (if previous exists)
    if('solvLabel' in locals()):
        solvLabel.destroy()
    val = solvable(newBoard)

    #creates new 'check inputs' label to update
    if(val == 1):
        val = "True"
    else:
        val = "False"
    solvLabel = Label(root, text = val, padx = 50, pady = 50)
    solvLabel.grid(row=20, column=4, columnspan=3)

#check final input, check proceeding inputs as well 
def finalCheck():
    final = entriesLabels[80].get()

    #final value is stored as 0 if blank
    if(len(final) == 0):
                final = 0

    #check all proceeding values are valid
    checkClick()
    val = 0
    rCount = 0

    #check for invalid input, including final input
    for r in newBoard:
        cCount = 0
        for c in r:
            if(c == 0):
                val = 0
            #check final value, check it is not blank
            if(rCount == 8 and cCount == 8 and final != 0):
                if(check_location(newBoard, 8, 8, final) == True):
                    val = 1
                if(check_location(newBoard, 8, 8, final) == False):
                    val = 0
            cCount+=1
        rCount+=1

    #delete old label to update (if previous exists)
    if('solvLabel2' in locals()):
        solvLabel2.destroy()

    #create new 'final check' label
    if(val == 1):
        val = "Winner!"
    else:
        val = "You lose!"

    solvLabel2 = Label(root, text = val, padx = 50, pady = 50, fg = 'red')
    solvLabel2.grid(row=20, column=11, columnspan=3)

#calls board mechanisms
def boardFunctions(entriesLabels):
    counter = 0
    #adds labels and entries to list
    for i in entriesLabels:
        value = 0
        #adds empty entries as 0 in list
        try:
            value = i.get()
            if(len(value) == 0):
                value = 0
        except:
            value = i
        newBoard[int(counter/9)][counter%9] = int(value)
        counter+=1

    #creates 'check inputs' and 'final check' buttons
    checkButton = Button(root, text = "Check Inputs", padx = 50, pady = 50, command = checkClick)
    checkButton.grid(row=20, column=0, columnspan=3)
    finalCheckButton = Button(root, text = "Final Check", padx = 50, pady = 50, command = finalCheck)
    finalCheckButton.grid(row = 20, column = 7, columnspan=3)

#creates sudoku board
def createBoard(diff):
    board = board5
    if(diff == 2):
        board = board5
    if(diff == 1):
        board = board3
    if(diff == 0):
        board = board1

    rowCount = 0
    print(board)

    #creating sudoku board of entries (blanks) and labels
    for r in board:
        colCount = 0
        #print("rowCount:" + str(rowCount))
        if(rowCount == 3 or rowCount == 7):
            vertLabel = Label(root, text = " ", width=5)
            rowCount+=1
            vertLabel.grid(row = rowCount, column = colCount, pady=5)
        for c in r:
            if(c == 0):
                blank = Entry(root, width=5, borderwidth=5)
                blank.grid(row = rowCount+1, column = colCount, pady=5)
                #adds to entries list
                entriesLabels.append(blank)
    
                if(colCount == 2 or colCount == 6):
                    horzLabel = Label(root, text = " ", width=5)
                    colCount+=1
                    horzLabel.grid(row = rowCount, column = colCount, pady=5)
            else:
                numLabel = Label(root, text = c, width=5, borderwidth=5)
                numLabel.grid(row = rowCount+1, column= colCount, pady=5)

                #adds to labels list
                numInt = numLabel.cget("text")
                entriesLabels.append(int(numInt))
               
                if(colCount == 2 or colCount == 6):
                    horzLabel = Label(root, text = " ", width=5)
                    colCount+=1
                    horzLabel.grid(row = rowCount, column = colCount, pady=5)
            colCount+=1
        rowCount+=1
    boardFunctions(entriesLabels)
    


#difficulty level buttons
def hardClick():
    hardButton.destroy()
    easyButton.destroy()
    intButton.destroy()
    diff = 2
    createBoard(2)

def intClick():
    hardButton.destroy()
    easyButton.destroy()
    intButton.destroy()
    diff = 1
    createBoard(1)

def easyClick():
    hardButton.destroy()
    easyButton.destroy()
    intButton.destroy()
    diff = 0
    createBoard(0)

#sudoku buttons 
hardButton = Button(root, text="Hard", padx=50, pady=50, command=hardClick)
intButton = Button(root, text="Intermediate", padx=50, pady=50, command=intClick)
easyButton = Button(root, text="Easy", padx=50, pady=50, command=easyClick)


#name button function
def myClick():
    name = "'s " + "Sudoku"
    myLabel = Label(root, text=e.get() + name)
    myButton.destroy()
    e.destroy()
    myLabel.grid(row = 0, column = 0, columnspan=4)
    sudokuButton()

#name button
myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick)
myButton.pack()

root.mainloop()

