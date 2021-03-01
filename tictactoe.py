import copy
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
        self.board=board 
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
        is_complete = None
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 0:
                    is_complete = False

        # Each possible board position is appended to the array.
        possible_board = []
        for rows in self.get_row(board):
            possible_board.append(rows)
        for columns in self.get_column(board):
            possible_board.append(columns)
        for diagonals in self.get_diagonal(board):
            possible_board.append(diagonal)

        # Count the number of empty squares, X's, and O's on the board.
        num_empty, num_X, num_O = 0
        for square in possible_board:
            if square == 0:
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
            for diagonals in self.get_diagonal(board):
                possible_board.append(diagonal)    

            # Count the number of empty squares, X's, and O's on the board.
            num_empty, num_X, num_O = 0
            for square in possible_board:
                if square == 0:
                    num_empty += 1
                elif square == 'X':
                    num_X += 1
                elif square == 'O':
                    num_O += 1
            
            # The winner is declared if the number of X's or O's in a row, column, or diagonal is 3.
            if num_X == 3:  
                return 'X'
            elif num_O == 3:
                return 'O'

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
        if board == 0:
            board = self.board

        #x1 = number of X's in corner pieces
        #x2 = number of O's in corner pieces
        #x3 = X in center; 1 if X, 0 if empty, -1 of O
        #x4 = O in center; 1 if O, 0 if empty, -1 if X
        #x5 = number of rows that have two X's
        #x6 = number of rows that have two O's
        #x7 = number of rows that have three X's
        #x8 = number of rows that have three O's
        #x5 = number of columns that have two X's
        #x6 = number of columns that have two O's
        #x7 = number of columns that have three X's
        #x8 = number of columns that have three O's
        
        x1 = 0      
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        x6 = 0
        x7 = 0
        x8 = 0
        x9 = 0
        x10 = 0
        x11 = 0
        x12 = 0

        #for x1 & x2
        for x in range(0,3,2):
            for y in range(0,3,2):
                if board[x][y]=='X':
                    x1 += 1
                elif board[x][y]=='O':
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
                x9 +=1
            if(num_X==3):
                x11 +=1
            if(num_O==2 and num_X==0):
                x10 +=1
            if(num_O==3):
                x12 +=1

        return x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
    
    def getSuccessors(self, symbol, board=0):
        if board == 0:
            board = self.board
        successors = []
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y]==" ":
                    successor = copy.deepcopy(board)
                    successor[x][y]=symbol
                    successors.append(successor)
        return successors

class Player:
    def __init__(self,board,symbol):
        self.board=board
        self.symbol=symbol
        self.weights=[0,0,0,0,0,0,0,0,0,0,0,0]

    def setLearningRate(self,lr):
        self.lr=lr

    def setBoard(self,board):
        self.board=board

    def setWeights(weights):
        self.weights=weights

    def evaluateBoard(self,board):
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12=self.board.getFeatures(board)
        w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12=self.weights

        return w1*x1+w2*x2+w3*x3+w4*x4+w5*x5+w6*x6+w7*x7+w8*x8+w9*x9+w10*x10+w11*x11+w12*x12

    def chooseMove(self):
        successors=self.board.getSuccessors(self.symbol)
        bestMove=successors[0]
        for successor in successors:
            if(self.evaluateBoard(successor)>self.evaluateBoard(bestMove)):
                bestMove=successor
                

        self.board.setBoard(bestMove)

    







#class Opponent:

b=Board()
b.create_board()
b.print_board()

#To test Board
# b.set_x(0,0)
# b.set_x(1,0)
# b.set_y(0,1)
# b.set_x(0,2)
# b.set_y(1,1)
# b.set_y(2,1)
# b.print_board()
# print(b.getFeatures())
# print(b.getSuccessors('X'))

#To Test Player
# Player1=Player(b,'X')
# Player1.chooseMove()
# Player1=Player(b,"O")
# Player1.chooseMove()
# b.print_board()
# Player1=Player(b,"X")
# Player1.chooseMove()
# Player1=Player(b,"O")
# Player1.chooseMove()
# b.print_board()
# Player1=Player(b,"X")
# Player1.chooseMove()
# Player1=Player(b,"O")
# Player1.chooseMove()
# b.print_board()








