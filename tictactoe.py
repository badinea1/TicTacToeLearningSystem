class GenerateBoard: # We may need to add methods to get features and successor states

    def initialize(self):
        self.board = self.create_board()

    def create_board(self): # Creates an array, with empty squares initialized to 0.
        board = [ [0,0,0],
                  [0,0,0],
                  [0,0,0] ]
        return board

    def set_x(self, x, y):
        self.board[x][y] = 'X'
    
    def set_y(self, x, y):
        self.board[x][y] = 'O'

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
            print "Game is incomplete. No winner determined."

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