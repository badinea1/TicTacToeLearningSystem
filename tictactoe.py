import copy
import random


class Board: 
    def __init__(self):
        self.board = self.create_board()
        self.playthrough = [copy.deepcopy(self.board)]

    def create_board(self): # Creates an array, with empty squares.
        board = [ [" "," "," "],
                  [" "," "," "],
                  [" "," "," "] ]
        return board

    def setBoard(self,board):
        self.board = board 
        self.playthrough.append(copy.deepcopy(self.board))

    def getPlaythrough(self):
        return self.playthrough
    
    def set_x(self, x, y):
        self.board[x][y] = 'X'
        self.playthrough.append(copy.deepcopy(self.board))
    
    def set_y(self, x, y):
        self.board[x][y] = 'O'
        self.playthrough.append(copy.deepcopy(self.board))

    def get_row(self, board = 0): # Returns each row of the board.
        if board == 0:
            board = self.board
        return board

    def get_column(self, board = 0): # Returns each column of the board.
        if board == 0:
            board = self.board

        possible_columns = []
        for x in range(len(board)):
            column = []
            column.append(board[0][x])
            column.append(board[1][x])
            column.append(board[2][x])
            possible_columns.append(column)
        return possible_columns

    def get_diagonal(self, board = 0): # Returns the diagonals of the board.
        if board == 0:
            board = self.board

        possible_diagonals = []

        L_to_R = []
        L_to_R.append(board[0][0])
        L_to_R.append(board[1][1])
        L_to_R.append(board[2][2])

        R_to_L = []
        R_to_L.append(board[2][0])
        R_to_L.append(board[1][1])
        R_to_L.append(board[0][2])

        possible_diagonals.append(L_to_R)
        possible_diagonals.append(R_to_L)
        return possible_diagonals

    def check_completion(self, board = 0): # Checks if the game is over.
        if board == 0:
            board = self.board

        # If there are empty squares in the board, the game is incomplete.
        is_complete = True
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == " ":
                    is_complete = False

        # Each possible board position is appended to the array.
        possible_board = []
        for rows in self.get_row(board):
            possible_board.append(rows)
        for columns in self.get_column(board):
            possible_board.append(columns)
        for diagonal in self.get_diagonal(board):
            possible_board.append(diagonal)

        #take 3 squares, then 

        # Count the number of empty squares, X's, and O's on the board.
        for line_of_squares in possible_board: 
            num_empty, num_X, num_O = 0, 0, 0
            for square in line_of_squares:
                if square == " ":
                    num_empty += 1
                elif square == 'X':
                    num_X += 1
                elif square == 'O':
                    num_O += 1
                # If the number of X's or O's in a row, column, or diagonal is 3, the game is complete.
                if (num_X == 3) or (num_O == 3):
                    is_complete = True

        return is_complete


    def assign_winner(self, board = 0): # Checks who won the game.
        if board == 0:
            board = self.board
        
        if self.check_completion(board): # If the game is complete.
            # Append each possible board position to the array.
            possible_board = []
            for rows in self.get_row(board):
                possible_board.append(rows)
            for columns in self.get_column(board):
                possible_board.append(columns)
            for diagonal in self.get_diagonal(board):
                possible_board.append(diagonal)    

            # Count the number of empty squares, X's, and O's on the board.
            for line_of_squares in possible_board: 
                num_empty, num_X, num_O = 0,0,0
                for square in line_of_squares:
                    if square == " ":
                        num_empty += 1
                    elif square == 'X':
                        num_X += 1
                    elif square == 'O':
                        num_O += 1

                if num_X == 3:  
                    return 1
                elif num_O == 3:
                    return 2
            
            # The winner is declared if the number of X's or O's in a row, column, or diagonal is 3.

            return 0
        else:
            print("Game is incomplete. No winner determined.")

    def print_board(self, board = 0): # The board is printed.
        if board == 0:
            board = self.board

        print('\n')
        print(board[0][0], '|', board[0][1], '|', board[0][2])
        print("-----")
        print(board[1][0], '|', board[1][1], '|', board[1][2])
        print("-----")
        print(board[2][0], '|', board[2][1], '|', board[2][2])
        print('\n')

    def getFeatures(self, board = 0):
        if board == 0:
            board = self.board
             
        x1 = 0  #number of X's in corner pieces
        x2 = 0  #number of O's in corner pieces
        x3 = 0  #X in center; 1 if X, 0 if empty, -1 of O
        x4 = 0  #O in center; 1 if O, 0 if empty, -1 if X
        x5 = 0  #number of rows that have two X's
        x6 = 0  #number of rows that have two O's
        x7 = 0  #number of rows that have three X's
        x8 = 0  #number of rows that have three O's
        x9 = 0  #number of columns that have two X's
        x10 = 0 #number of columns that have two O's
        x11 = 0 #number of columns that have three X's
        x12 = 0 #number of columns that have three O's

        #for x1 & x2
        for x in range(0,3,2):
            for y in range(0,3,2):
                if board[x][y] == 'X':
                    x1 += 1
                elif board[x][y] == 'O':
                    x2 += 1

        #for x3 & x4
        if board[1][1] == 'X':
            x3 += 1
            x4 += -1
        elif board[1][1] == 'O':
            x4 += 1
            x3 += -1

      
        for x in range(len(board)):
            num_X = 0
            num_O = 0
            for y in range(len(board)):
                if board[x][y] == 'X':
                    num_X += 1
                if board[x][y] == 'O':
                    num_O += 1
            if(num_X==2 and num_O==0 ):
                x5 +=1
            if(num_X==3):
                x7 +=1
            if(num_O==2 and num_X==0):
                x6 +=1
            if(num_O==3):
                x8 +=1
                
        for x in range(len(board)):
            num_X = 0
            num_O = 0
            for y in range(len(board)):
                if board[y][x] == 'X':
                    num_X += 1
                if board[y][x] == 'O':
                    num_O += 1
            if(num_X==2 and num_O==0):
                x9 += 1
            if(num_X==3):
                x11 += 1
            if(num_O==2 and num_X==0):
                x10 += 1
            if(num_O==3):
                x12 += 1

        return x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
    
    def getSuccessors(self, symbol, board=0):
        if board == 0:
            board = self.board
        successors = []
        for x in range(len(board)):
            for y in range(len(board)):
                if self.board[x][y]== " ":
                    successor = copy.deepcopy(self.board)
                    successor[x][y] = symbol
                    successors.append(successor)
        return successors
        
    def getTrainingData(self,playthrough,player):
        trainingData = []

        for i in range(0,len(playthrough)):
            if(self.check_completion(playthrough[i])):
                if(self.assign_winner(playthrough[i]) == player.symbol):
                    trainingData.append([self.getFeatures(playthrough[i]), 100])
                elif(self.assign_winner(playthrough[i]) == 0):
                    trainingData.append([self.getFeatures(playthrough[i]), 0])
                else:
                    trainingData.append([self.getFeatures(playthrough[i]), -100])
            else:
                if i+2 >= len(playthrough):
                    if(self.assign_winner(playthrough[len(playthrough)-1]) == 0):
                        trainingData.append([self.getFeatures(playthrough[i]), 0])
                    else:
                        trainingData.append([self.getFeatures(playthrough[i]), -100])
                else:
                    trainingData.append([self.getFeatures(playthrough[i]), player.evaluateBoard(playthrough[i+2])])

        return trainingData

class Player:
    def __init__(self,board,weights,symbol):
        self.board = board
        self.symbol = symbol
        self.weights = weights
        self.lr = .1

    def setLearningRate(self,lr):
        self.lr = lr

    def setBoard(self,board):
        self.board = board

    def getBoard(self):
        return self.board

    def setWeights(self, weights):
        self.weights = weights

    def getWeights(self):
        return self.weights

    def evaluateBoard(self,board):
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = self.board.getFeatures(board)
        w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12 = self.weights

        return w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10 + w11*x11 + w12*x12

    # updating weights using LMS rule
    def LMS(self,playthrough,trainingData):
        for i in range(0,len(playthrough)):
            w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12 = self.weights
            vHat = self.evaluateBoard(playthrough[i])
            x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = trainingData[i][0]
            vTrain = trainingData[i][1]            

            w0 = w0 + self.lr*(vTrain - vHat)
            w1 = w1 + self.lr*(vTrain - vHat)*x1
            w2 = w2 + self.lr*(vTrain - vHat)*x2
            w3 = w3 + self.lr*(vTrain - vHat)*x3
            w4 = w4 + self.lr*(vTrain - vHat)*x4
            w5 = w5 + self.lr*(vTrain - vHat)*x5
            w6 = w6 + self.lr*(vTrain - vHat)*x6
            w7 = w7 + self.lr*(vTrain - vHat)*x7
            w8 = w8 + self.lr*(vTrain - vHat)*x8
            w9 = w9 + self.lr*(vTrain - vHat)*x9
            w10 = w10 + self.lr*(vTrain - vHat)*x10
            w11 = w11 + self.lr*(vTrain - vHat)*x11
            w12 = w12 + self.lr*(vTrain - vHat)*x12


            self.weights = w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12

    #think we have to fix this
    def chooseMove(self):
        successors = self.board.getSuccessors(self.symbol)
        bestMove = successors[0]
        bestOption = self.evaluateBoard(bestMove)
        for successor in successors:
            if(self.evaluateBoard(successor)>bestOption):
                bestOption = self.evaluateBoard(successor)
                bestMove = successor
                
        self.board.setBoard(bestMove)
    


b = Board()
b.create_board()
b.print_board()

weights1 = (.3,.3,.3,.3,.3,.3,.3,.3,.3,.3,.3,.3,.3)
weights2 = (.3,-10,10,-10,10,-10,10,-10,10,-10,10,-10,10)

learner = Player(b, weights1, 'X')
opponent = Player(b, weights2, 'O')

opponent.setLearningRate(0)

# system1 = System(b, weights1, 'X')
# system2 = System(b, weights2, 'O')

X_wins = 0
O_wins = 0
tie = 0

for i in range(0,10):
    b = Board()
    learner.setBoard(b)
    opponent.setBoard(b)

    while(not b.check_completion()):
        learner.chooseMove()
        b.print_board()
        if b.check_completion():
            #b.print_board()
            break
        opponent.chooseMove()
        b.print_board()


    winner = b.assign_winner()
            
    if(winner == 1):
        print ("X wins")
        X_wins += 1
    elif(winner == 2):
        print ("O wins")
        O_wins += 1
    elif(winner == 0):
        print ("The game is a tie.")
        tie += 1


    learner.LMS(b.getPlaythrough(),b.getTrainingData(b.getPlaythrough(),learner))
    #opponent.LMS(b.getPlaythrough(),b.getTrainingData(b.getPlaythrough(),learner))

    print ("X won " + str(X_wins) + " games.")
    print ("O won " + str(O_wins) + " games.")
    print ("There were " + str(tie) + " ties.")


    print("DONEEEEE")
    print ("L", learner.getWeights())
    print ("O", opponent.getWeights())
