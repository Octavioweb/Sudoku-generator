#Juego que genera un mapa de sudoku
import random, string, math, sys

size = 16

assert (math.sqrt(size) %1 == 0) , ('Size must be a perfect square!')

#Generates a list of size (size) to use with random
numbers = []
nums = string.printable
for pos in range (1, size+1):
    numbers.append(nums[pos])
    
#Generate empty board
board = []
row = []
for i in range(size):
    for j in range(size):
        row.append('0')
    board.append(row)
    row = []

def Main(board):
    board_save = board
    row = []
    row2 = ['0' for a in range (size)]
    j = 0
    errorCount=0

    while j < (size):
        while True:    
            try:
                for i in range(size):
            
                    num_temp = set(numbers)
                    
                    #Generate list (set) of adjacent numbers
                    baadSet = GetForbiddenSet(board, size, i, j)
                    randOptions = (num_temp - baadSet)
                    options = list(randOptions)
                    rand = random.choice(options)
                    
                    board[j][i] = rand
                board_save = board
                j +=1
                
            except IndexError:
                    errorCount += 1
                    if errorCount > 20*size**2:
                        print ('Errores = ', errorCount)
                        board = []
                        row = []
                        for i in range(size):
                            for j in range(size):
                                row.append('0')
                            board.append(row)
                            row = []
                        Main(board)

                    try: 
                        board[j][:] = row2
                    
                        break
                    except IndexError:
                        printBoard(board, squareSize)
                        sys.exit()
            
        row = []
                
#Function called inside function of forbidden set        
def GetSquare(board, size, i, j):
    global limits, squareSize 
    squareSize = int(math.sqrt(size))
    squares = {}
    
    limits = []
    a_0 = 0
    HCoord = 0
    VCoord = 0
    
    for a in range (squareSize):
        limits.append(a*squareSize)
        
    for p in range (squareSize-1,0,-1):
        if i >= limits[p]:
            HCoord = p
            break
        else:
            continue

    for q in range (squareSize-1,0,-1):
        if j >= limits[q]:
            VCoord = q
            break
        else:
            continue
        
    return (HCoord, VCoord)
            
def GetForbiddenSet(board, size, i, j):
    global numTempX, numTempY, squareSet
    HCoord, VCoord = GetSquare(board, size, i, j)
    
    xCoord = HCoord*squareSize
    yCoord = VCoord*squareSize
    
    numTempY = set(board[j][:])
    numTempX = {'0'}
    for u in range(size):
        numTempX.add(board[u][i])
    
    squareSet = {'0'}
    for p in range (squareSize):
        for q in range (squareSize):
            squareSet.add(board[yCoord+p][xCoord+q])
            #print ('Coords = ', board[yCoord+p][xCoord+q])
    badSet = (numTempX | numTempY | squareSet)
    return badSet
                
def printBoard (sudoku, squareSize):
    linVerti = 0
    linHori = 0
    
    for line in sudoku:
        for char in line:
            linVerti+=1
            print (char, end =' ')
            if linVerti == squareSize:
                print ('|', end = ' ')
                linVerti= 0
        linHori +=1
        if linHori == squareSize:
            linHoriVer = 0
            print()
            for i in range(len(sudoku)):
                
                if linHoriVer == squareSize:
                    print ('  ', end = '')
                    linHoriVer = 0
                print('-', end= ' ')
                linHori = 0
                linHoriVer +=1
        print()                

Main(board)     
