import copy

class Board: 
    def __init__(self):
        self.board = self.create_board()    #to generate a board 
        self.playthrough = [copy.deepcopy(self.board)] #to keep track of our game history

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

        # If there are empty squares in the board, the game may be incomplete.
        is_complete = True
        for x in range(len(board)): # if the position (x,y) in board is empty for all x & y in their range, then the game may not be complete.
            for y in range(len(board)):
                if board[x][y] == " ":
                    is_complete = False

        # Each possible board position is appended to the array.
        possible_board = []
        for rows in self.get_row(board):
            possible_board.append(rows)         #append the rows 
        for columns in self.get_column(board):  #append the columns 
            possible_board.append(columns)
        for diagonal in self.get_diagonal(board):    #append the diagonals
            possible_board.append(diagonal)

        #Take 3 squares, then count the number of empty squares, X's, and O's among them.
        for line_of_squares in possible_board: 
            num_empty, num_X, num_O = 0, 0, 0
            for square in line_of_squares:
                if square == " ":   #if square is empty, update counter 
                    num_empty += 1
                elif square == 'X': #if there is an X in the square, update counter
                    num_X += 1
                elif square == 'O': #if there is an O in the square, update counter
                    num_O += 1
                # If the number of X's or O's in a row, column, or diagonal is 3, the game is complete.
                if (num_X == 3) or (num_O == 3):
                    is_complete = True

        return is_complete


    def assign_winner(self, board = 0): # Checks who won the game.
        if board == 0: #default board value
            board = self.board
        
        if self.check_completion(board): # if the game is complete.
            # Append each possible board position to the array.
            possible_board = []
            for rows in self.get_row(board):
                possible_board.append(rows) # append rows
            for columns in self.get_column(board):
                possible_board.append(columns)  # append columns
            for diagonal in self.get_diagonal(board):
                possible_board.append(diagonal)  # append diagnols  

            #Take 3 squares, then count the number of empty squares, X's, and O's among them.
            for line_of_squares in possible_board: 
                num_empty, num_X, num_O = 0,0,0
                for square in line_of_squares:
                    if square == " ":   #if a square is empty, update counter
                        num_empty += 1
                    elif square == 'X': #if there is an X, update counter 
                        num_X += 1
                    elif square == 'O': #if there is an O, update counter
                        num_O += 1

                if num_X == 3: #if X wins 
                    return 1
                elif num_O == 3: #if O wins
                    return 2
            
            # The winner is declared if the number of X's or O's in a row, column, or diagonal is 3.

            return 0
        else:
            print("Game is incomplete. No winner determined.")

    def print_board(self, board = 0): # The board is printed.
        if board == 0:
            board = self.board

        print('\n')
        print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
        print("-----")
        print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
        print("-----")
        print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
        print('\n')

    def getFeatures(self, board = 0):
        if board == 0: #default board value
            board = self.board
             
        x1 = 0  #number of X's in corner positions
        x2 = 0  #number of O's in corner positions
        x3 = 0  #X in center; 1 if X, 0 if empty, -1 if O
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
        for x in range(0,3,2): #for all x in the range and for all y in the range, check if board at (x,y) is X. Then, update the respective features depending on the outcome.
            for y in range(0,3,2):
                if board[x][y] == 'X':
                    x1 += 1
                elif board[x][y] == 'O':
                    x2 += 1

        #for x3 & x4
        if board[1][1] == 'X': #Check if board at (1,1) is X. Then, update the respective features depending on the outcome.
            x3 += 1
            x4 += -1
        elif board[1][1] == 'O':
            x4 += 1
            x3 += -1

        #for x5, x6, x7 & x8
        for x in range(len(board)):
            num_X = 0 # counters that keep track of how many X's and O's there are on the board for each row
            num_O = 0
            for y in range(len(board)): # for all x in the range, for all y in the range, check the following at board position (x,y) 
                if board[x][y] == 'X':
                    num_X += 1
                if board[x][y] == 'O':
                    num_O += 1
            if(num_X==2 and num_O==0): #if there are two X's and no O's, then update respective feature
                x5 +=1
            if(num_X==3): #if there are three X's in a row, then update respective feature
                x7 +=1
            if(num_O==2 and num_X==0): #if there are two O's and no X's in a row, then update respective feature
                x6 +=1
            if(num_O==3): #if there are three O's in a row, then update respective feature
                x8 +=1
        
         #for x9, x10, x11 & x12        
        for x in range(len(board)): # counters that keep track of how many X's and O's there are on the board for each column
            num_X = 0
            num_O = 0
            for y in range(len(board)): # for all x in the range and for all y in the range, check the following at board position (x,y) 
                if board[y][x] == 'X':
                    num_X += 1
                if board[y][x] == 'O':
                    num_O += 1
            if(num_X==2 and num_O==0): #if there are two X's and no O's, then update respective feature
                x9 += 1
            if(num_X==3): #if there are three X's in a row, then update respective feature
                x11 += 1
            if(num_O==2 and num_X==0): #if there are two O's and no X's in a row, then update respective feature
                x10 += 1
            if(num_O==3): #if there are three O's in a row, then update respective feature
                x12 += 1

        return x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
    
    def getSuccessors(self, symbol, board=0): #returns successive board states
        if board == 0: #default board value
            board = self.board
        successors = []
        for x in range(len(board)):
            for y in range(len(board)):
                if self.board[x][y]== " ": #if current board position is empty
                    successor = copy.deepcopy(self.board) #make copy of current board
                    successor[x][y] = symbol #change empty position to player's symbol in order to represent successive state
                    successors.append(successor) #Add to list of successors
        return successors
        
    def getTrainingData(self,playthrough,player): #To extract training data from games played
        trainingData = []
        
        # iterate through the playthrough
        for i in range(0,len(playthrough)):
            # for completed board states
            if(self.check_completion(playthrough[i])):
                if(self.assign_winner(playthrough[i]) == player.symbol):
                    trainingData.append([self.getFeatures(playthrough[i]), 100]) #if player is the winner of the game, assign each board state in this playthrough a value of 100
                elif(self.assign_winner(playthrough[i]) == 0):
                    trainingData.append([self.getFeatures(playthrough[i]), 0]) #if the game was a tie, assign each board state in this playthrough a value of 0
                else:
                    trainingData.append([self.getFeatures(playthrough[i]), -100]) #if the opponent is the winner of the game, assign each board state in this playthrough a value of -100
            else:
                # for board states that are not completed
                if i+2 >= len(playthrough): 
                    if(self.assign_winner(playthrough[len(playthrough)-1]) == 0): # looks at the last game in the playthrough
                        trainingData.append([self.getFeatures(playthrough[i]), 0])
                    else:
                        trainingData.append([self.getFeatures(playthrough[i]), -100]) # adjusts features 
                else:
                    trainingData.append([self.getFeatures(playthrough[i]), player.evaluateBoard(playthrough[i+2])]) # chooses two states ahead of the current board state

        return trainingData

class Player: 
    def __init__(self,board,weights,symbol):
        self.board = board
        self.symbol = symbol
        self.weights = weights
        self.lr = .1  #this is a small constant that moderates the size of the weight update

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
    def LMS(self,playthrough,trainingData): #Originally, we realized that we didn't include w0 and our ratio of games won and games lost was very close. Once, we added w0 the ratio was more of what we expected. 
        for i in range(0,len(playthrough)):
            w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12 = self.weights
            vHat = self.evaluateBoard(playthrough[i])
            x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = trainingData[i][0]
            vTrain = trainingData[i][1]            

            # this is based on the LMS algorithm given to us in class
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

    #this function chooses moves by evaluating the current board's successors
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

weights1 = (.3,.3,.3,.3,.3,.3,.3,.3,.3,.3,.3,.3,.3) # Starting weights of learner
weights2 = (.3,-10,10,-10,10,-10,10,-10,10,-10,10,-10,10) #Constant weights of opponent

learner = Player(b, weights1, 'X') # Learner always is 'X'
opponent = Player(b, weights2, 'O') # Opponent always is 'O'

#To keep track of game outcomes
X_wins = 0
O_wins = 0
tie = 0

#Gameplay begins
for i in range(0,10000): #The upper bound of this range dictates the number of games played
    b = Board()
    b.create_board()
    b.print_board()
    learner.setBoard(b)
    opponent.setBoard(b)

    while(not b.check_completion()):
        learner.chooseMove()
        b.print_board()
        if b.check_completion():
            break
        opponent.chooseMove()
        b.print_board()


    winner = b.assign_winner()
            
    if(winner == 1): #if X wins, update counter
        print ("X wins")
        X_wins += 1
    elif(winner == 2): #if O wins, update counter
        print ("O wins")
        O_wins += 1
    elif(winner == 0): #if game is a tie, update counter
        print ("The game is a tie.")
        tie += 1


    learner.LMS(b.getPlaythrough(),b.getTrainingData(b.getPlaythrough(),learner))

    print ("X won " + str(X_wins) + " games.")
    print ("O won " + str(O_wins) + " games.")
    print ("There were " + str(tie) + " ties.")

    print ("L", learner.getWeights())
    print ("O", opponent.getWeights())
