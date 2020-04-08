
###import
import random


###variables

mineFound = False
x = 0
y = 0
boardX = 4
boardY = 4
m = False
h = True
v = 0
findX = 0
findY = 0
mineFound = False

###Functions
 
def initBoard(x1,y1):   
    a = []
    for y in range(y1):
        for x in range(x1):
            a.append((x,y,m,h,v))
    return a

def getValue(x,y,board):
    for i in board:
        (x1,y1,m,h,v)=i
        if x1 == x and y1 == y:
            return v
    return "error"

def placeMines(bn,bX,bY,nm,board):
    for i in range(nm): # Creates mines in requsted amount of mines (nm)
        i1 = True#setups while loop
        i2 = True#setups while loop
        i3 = True#setups while loop
        while i3 == True:#gets a block to make mine
            r = random.randint(0,len(board)-1)#gets random number in board list
            if r != bn-bX-1 and r != bn-bX and r != bn-bX+1 and r != bn-1 and r != bn and r != bn+1 and r != bn+bX-1 and r != bn+bX and r != bn+bX+1:#checks bn and surrounding blocks
                i1 = False
            if board[r][2] == False: #Checks if tuple already is mine
                i2 = False
            if i1 == False and i2 == False:#Confirms that block is not mine and is not bn or surrounding blocks
                i3 = False
            else:
                i1 = True
                i2 = True
        (x,y,m,h,v)=board.pop(r) #Takes out tuple from list
        board.insert(r, (x,y,True,h,v)) # Inserts modified tuple
    return board
    
def printInitBoard(x,y,board):   
    x1 = 0
    for i in range(y):
        for i1 in range(x):            
            print(board[x1], end = "")
            x1 = x1+1
        print()   

def assignValue(x,y,board):
    i = 0
    i3 = 0
    
    for i1 in board:
        i3 = 0
        a = []
        v = 0
        t = list(board[i])
        if t[4] == 0:
            if t[0] == 0 and t[1] == 0: #tl
                a.append(board[i+1])#r
                a.append(board[i+x])#b
                a.append(board[i+x+1])#br
            if t[0] > 0 and t[0] < x-1 and t[1] == 0: #t
                a.append(board[i-1])#l
                a.append(board[i+1])#r
                a.append(board[i+x-1])#bl
                a.append(board[i+x])#b
                a.append(board[i+x+1])#br
            if t[0] == x-1 and t[1] == 0: #tr
                a.append(board[i-1])#l                
                a.append(board[i+x-1])#bl
                a.append(board[i+x])#b
            if t[0] == 0 and t[1] > 0 and t[1] < y-1: #l
                a.append(board[i-x])#t
                a.append(board[i-x+1])#tr
                a.append(board[i+1])#r
                a.append(board[i+x])#b
                a.append(board[i+x+1])#br
            if t[0] == x-1 and t[1] > 0 and t[1] < y-1: #r
                a.append(board[i-x-1])#tl
                a.append(board[i-x])#t
                a.append(board[i-1])#l
                a.append(board[i+x-1])#bl
                a.append(board[i+x])#b
            if t[0] == 0 and t[1] == y-1: #bl
                a.append(board[i-x])#t
                a.append(board[i-x+1])#tr
                a.append(board[i+1])#r
            if t[0] > 0 and t[0] < x-1 and t[1] == y-1: #b
                a.append(board[i-x-1])#tl
                a.append(board[i-x])#t
                a.append(board[i-x+1])#tr
                a.append(board[i-1])#l
                a.append(board[i+1])#r
            if t[0] == x-1 and t[1] == y-1: #br
                a.append(board[i-x-1])#tl
                a.append(board[i-x])#t
                a.append(board[i-1])#r
            if t[0] > 0 and t[0] < x-1 and t[1] > 0 and t[1] < y-1: #ordinary
                a.append(board[i-x-1])#tl
                a.append(board[i-x])#t
                a.append(board[i-x+1])#tr
                a.append(board[i-1])#l
                a.append(board[i+1])#r
                a.append(board[i+x-1])#bl
                a.append(board[i+x])#b
                a.append(board[i+x+1])#br
            for i2 in a:
                if a[i3][2] == True:
                    v = v+1
                i3 = i3+1
            t[4] = v
            l = tuple(t)
        board.pop(i)
        board.insert(i, l)
        i = i+1

def printBoard(x,y,mf,board):
    objectX = 0
    objectY = 0
    i = 0
    for iy in range(y):
        objectX = 0
        for ix in range(x):
            ft = True
            while ft == True:
                if board[i][0] == objectX and board[i][1] == objectY: #Find the right tuple
                    if board[i][3] == True: # Found tuple and printed hidden
                        xPrint = str(objectX)
                        yPrint = str(objectY)
                        print("["+xPrint+","+yPrint+"]", end = "")
                    if board[i][3] == False and board[i][2] == False: # Found tuple and printed value
                        bPrint = str(board[i][4])
                        print("["+bPrint+"]", end = "")
                    if board[i][3] == False and board[i][2] == True: #Found Mine
                        print("[M]", end = "")
                    ft = False
                else: #Didn't find tuple
                    i = i + 1
            objectX = objectX + 1
        print()
        objectY = objectY + 1

def askBlock(x, y):
    done = True
    while done == True:
        wXstr = input("what x?  ")
        try:
            wX = int(wXstr)
            if wX >= 0 and wX < x:
                findX = wX
                done = False
            else:
                print("Try again")
        except:
            print("Try again")
    done = True
    while done == True:
        wYstr = input("what y?  ")
        try:
            wY = int(wYstr)
            if wY >= 0 and wY < y:
                findY = wY
                done = False
            else:
                print("Try again")
        except:
            print("Try again")
    return findX, findY

def getBlock(findX,findY,board):
    bn = 0
    i = True
    while i == True:
        if board[bn][0] == findX and board[bn][1] == findY:
            block = (board[bn])
            i = False
        else:
            bn = bn + 1
    return bn

def processBlock(mf,bn,board):
    # l = []
    if board[bn][2] == True:
        mf = True
    # if board[bn][2] == False:
    l = list(board[bn])
    l[3] = False
    t = tuple(l)
    board.pop(bn)
    board.insert(bn, t) # make visible
    if mf == True:
        lose = True
    else:
        lose = False
    return mf, lose
    
def boardSizeMines():
    i = True
    while i == True:
        bXstr = input("Board x?  ")
        try:
            bX = int(bXstr)
            i = False
        except:
            print("Try Again")
    i = True
    while i == True:
        bYstr = input("Board Y?  ")
        try:
            bY = int(bYstr)
            i = False
        except:
            print("Try again")    
    i = True
    while i == True:
        bMstr = input("How many mines?  ")
        try:
            bM = int(bMstr)
            if bM <= bX * bY:
                i = False
            else:    
                print("Try again")
        except:
            print("Try again")
    return bX, bY, bM

def cleanZeroes(x,y,bn,boardReal):
    
    board = boardReal
    repeat = True
    iR = 0    
    while repeat == True:   
        for iR in range(y):
            iN = 0       
            for i in board:  
                if board[iN][4] == 0 and board[iN][3] == False:
                    if board[iN][0] == 0 and board[iN][1] == 0: #tl
                        i2 = iN+1#r
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x#b
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x+1#br
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] > 0 and board[iN][0] < x-1 and board[iN][1] == 0: #t
                        i2 = iN-1#l
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+1#r¨
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+x-1#bl
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x#b
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x+1#br
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] == x-1 and board[iN][1] == 0: #tr
                        i2 = iN-1#l
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x-1#bl
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x#b
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] == 0 and board[iN][1] > 0 and board[iN][1] < y-1: #l
                        i2 = iN-x#t
                        board = changeTupleIfZero(i2,board)
                        i2 = iN-x+1#tr
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+1#r
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x#b
                        board = changeTupleIfZero(i2,board)
                        i2 = iN+x+1#br
                        board = changeTupleIfZero(i2,board)     
                    if board[iN][0] == x-1 and board[iN][1] > 0 and board[iN][1] < y-1: #r
                        i2 = iN-x-1#tl
                        board = changeTupleIfZero(i2,board)
                        i2 = iN-x#t
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-1#l
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+x-1#bl
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+x#b
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] == 0 and board[iN][1] == y-1: #bl
                        i2 = iN-x#t
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-x+1#tr
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+1#r
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] > 0 and board[iN][0] < x-1 and board[iN][1] == y-1: #b
                        i2 = iN-x-1#tl
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-x#t
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-x+1#tr
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-1#l
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+1#r
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] == x-1 and board[iN][1] == y-1: #br
                        i2 = iN-x-1#tl
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-x#t
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-1#r
                        board = changeTupleIfZero(i2,board)
                    if board[iN][0] > 0 and board[iN][0] < x-1 and board[iN][1] > 0 and board[iN][1] < y-1: #ordinary
                        i2 = iN-x-1#tl
                        changeTupleIfZero(i2,board)
                        i2 = iN-x#t
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-x+1#tr
                        board = changeTupleIfZero(i2,board)

                        i2 = iN-1#l
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+1#r
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+x-1#bl
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+x#b
                        board = changeTupleIfZero(i2,board)

                        i2 = iN+x+1#br
                        board = changeTupleIfZero(i2,board)                
                iN = iN + 1
        if board != boardReal:
            boardReal = board
        else:
            repeat = False
    return boardReal

def changeTupleIfZero(i2,board):
    l = list(board[i2])
    l[3] = False
    t = tuple(l)
    board.pop(i2)
    board.insert(i2, t)
    return board

def sortList(x,y,board):
    a = []
    ry =0
    for i in range(y):
        rx = 0
        for i1 in range(x):
            nl = board.index((rx,ry,m,h,v))
            a.append(board[nl])
            rx = rx+1
        ry = ry+1
    return a

def clearLostBoard(board):
    i = 0 
    for i1 in board:
        l = list(board[i])
        l[3] = False
        t = tuple(l)
        board.pop(i)
        board.insert(i, t)
        i = i+1
    return board

def checkNumberOfNonMines(board):
    i = 0
    nNM = 0
    for i1 in board:
        if board[i][2] == False:
            nNM = nNM + 1
        i = i + 1
    return nNM

def winFunction(win,nNM,board):
    win = False
    i = 0
    nF = 0
    for i1 in board:
        if board[i][3] == False:
            nF = nF+1 
        i=i+1
    if nNM == nF:
        win = True
    else:
        win = False
   
    return win

###Main

# print(board)
# print(getValue(2,3,board))






### Setup
gameOver = False

win = False

boardX, boardY, boardMines = boardSizeMines() #creates board size

board = initBoard(boardX,boardY) #creates blocks in list

sortList(boardX,boardY,board)

# print(board) # If you want to check cheat sheet

printBoard(boardX,boardY,mineFound,board) #prints game board

findX, findY = askBlock(boardX,boardY) #asks for what block

askForBlock = False

requestedBlockNumber = getBlock(findX,findY,board) 

board = placeMines(requestedBlockNumber,boardX,boardY,boardMines,board) # assigns mines to list

assignValue(boardX,boardY,board) #gives every block a value

numberOfNonMines = checkNumberOfNonMines(board) #Counts the number of normal blocks


# printInitBoard(boardX,boardY,board) #prints cheat board


### GAME


while gameOver == False: # the game loop
    if askForBlock == True:
        findX, findY = askBlock(boardX,boardY) #asks for what block
    getBlock(findX,findY,board) #gets the block ur looking for
    requestedBlockNumber = getBlock(findX,findY,board) #Finds the right block in list
    mineFound, lose = processBlock(mineFound,requestedBlockNumber,board) #Checks if block is mine or what value block gets(if it's mine it'll make lose = true)
    board = cleanZeroes(boardX,boardY,requestedBlockNumber,board) #If requested block is zero it'll clear all surrounding zeroes
    printBoard(boardX,boardY,mineFound,board) # will print the game boiard    
    win = winFunction(win,numberOfNonMines,board) #will check if player has gotten all normal blocks
    if win == True or lose == True: # checks if player has won or lost
        gameOver = True #cancels loop
    askForBlock = True #makes sure you can play multiple round (see first line in loop)


board = clearLostBoard(board)
printBoard(boardX,boardY,mineFound,board)
if lose == True:
    print("LOSE")
if win == True:
    print("WIN")

# checkBlock(findX,findY,board)


##not used
# placeMines(1,a)
# print(a[3][2])

###dummy
# func placemines(nm,board):
#     if board[1][3] == False
#         board[1][3] = true 