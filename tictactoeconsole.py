Board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

CurrentPlayer = "X"
winner = None
gamerunning = True

def printBoard(Board):
    print(Board[0] + " | " + Board[1] + " | " + Board[2])
    print("-----------")
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print("-----------")
    print(Board[6] + " | " + Board[7] + " | " + Board[8])
    

def playerInput(Board):
    inp = int(input("Enter a number from 1-9:"))
    if inp >= 1 and inp <= 9 and Board[inp-1] == "-":
        Board[inp-1] = CurrentPlayer
    else:
        print("already taken")

def checkDown(Board):
    global winner
    if Board[0] == Board[3] == Board[6] and Board[0] != "-":
        winner = Board[0]
        return True
    elif Board[1] == Board[4] == Board[7] and Board[1] != "-":
        winner = Board[1]
        return True
    elif Board[2] == Board[5] == Board[8] and Board[2] != "-":
        winner = Board[2]
        return True
    
def checkHorizontal(Board):
     global winner
     if Board[0] == Board [1] == Board[2] and Board[0] != "-":
         winner = Board[0]
         return True
     elif Board[3] == Board[4] == Board[5] and Board[3] != "-":
         winner = Board[3]
         return True
     elif Board[6] == Board[7] == Board[8] and Board[6] != "-":
         winner = Board[6]
         return True

def checkDiag(Board):
    global winner 
    if Board[0] == Board [4] == Board[8] and Board[0] != "-":
        winner = Board[0]
        return True
    elif Board[2] == Board[4] == Board[6] and Board[2]!= "-":
        winner = Board[2]
        return True
    
def checkwin():
    global gamerunning
    if checkDiag(Board) or checkDown(Board) or checkHorizontal(Board):
        print("the winner is " + winner)
        gamerunning = False
    
def switchplayer():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer ="X"
    
def checkTie(Board):
    global gamerunning
    if "-" not in Board:
        printBoard(Board)
        print("it is a tie")
        gamerunning = False
    






while gamerunning:
    printBoard(Board)
    playerInput(Board)
    checkwin()
    checkTie(Board)
    
    if gamerunning:
        switchplayer()





                         


