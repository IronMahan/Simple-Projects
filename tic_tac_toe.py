class Board:
    def __init__(self, comp, opponent, null):
        self.board = [[null for _ in range(3)] for _ in range(3)]
        self.maxP = comp
        self.minP = opponent
        self.null = null
    
    def isTerminal(self, state):
        if self.result(state) not in [-10, 10]:
            for row in state:
                if self.null in row:
                    return False
        return True

    def validActions(self, state):
        act = []
        for row in range(3):
            for col in range(3):
                if state[row][col] == self.null:
                    act.append([row, col])
        return act

    def result(self, state):
        for row in state:
            if (row[0] == row[1] == row[2]) and (row[0] != self.null):
                return 10 if row[0] == self.maxP else -10
            
        for col in list(zip(*state)):
            if (col[0] == col[1] == col[2]) and (col[0] != self.null):
                return 10 if col[0] == self.maxP else -10
                
            
        if (state[0][0] == state[1][1] == state[2][2]) and (state[0][0] != self.null):
            return 10 if state[0][0] == self.maxP else -10
        
        elif (state[0][2] == state[1][1] == state[2][0]) and (state[0][2] != self.null):
            return 10 if state[0][2] == self.maxP else -10
        
        else:
            return 0
    
    def minimax(self, state, player):
        if self.isTerminal(state):
            return self.result(state)
        
        if player == self.maxP:
            value = float('-inf')
            for row, col in self.validActions(state):
                # print(row, col)
                state[row][col] = self.maxP
                res = self.minimax(state, self.minP)
                if res > value:
                    value = res
                state[row][col] = self.null
            
            return value
        
        else:
            value = float('inf')
            for row, col in self.validActions(state):
                state[row][col] = self.minP
                res = self.minimax(state, self.maxP)
                if res < value:
                    value = res
                state[row][col] = self.null

            return value
    

    
    def render(self):
        for row in self.board:
            print('|'.join(row))


if __name__ == '__main__':
    myBoard = Board('x', 'o', '-')

    for _ in range(9):

        print('\nYour turn')
        while True:    
            uRow, uCol = eval(input("Enter row, col: "))
            if [uRow, uCol] in myBoard.validActions(myBoard.board):
                break
        myBoard.board[uRow][uCol] = myBoard.minP
        myBoard.render()

        print("\nBot's turn")


        if (not myBoard.validActions(myBoard.board)) or (myBoard.result(myBoard.board) in [10, -10]):
            r = myBoard.result(myBoard.board)
            print("Score is:", r)
            match r:
                case 10:
                    print("Bot won!")
                case -10:
                    print("You won!")
                case _:
                    print("Tie")
            
            break

        # print('\nYour turn')
        # while True:    
        #     uRow, uCol = eval(input("Enter row, col: "))
        #     if [uRow, uCol] in myBoard.validActions(myBoard.board):
        #         break
        # myBoard.board[uRow][uCol] = myBoard.minP
        # myBoard.render()

        # print("\nBot's turn")

        # Find best move 
        actions = myBoard.validActions(myBoard.board)
        maxScore = float('-inf')
        for action in actions:
            myBoard.board[action[0]][action[1]] = myBoard.maxP
            score = myBoard.minimax(myBoard.board, myBoard.minP)
            myBoard.board[action[0]][action[1]] = myBoard.null
            if score > maxScore:
                bestMove = action
                maxScore = score
        print('-'*3)
        myBoard.board[bestMove[0]][bestMove[1]] = 'x'
        myBoard.render()

        if (not myBoard.validActions(myBoard.board)) or (myBoard.result(myBoard.board) in [10, -10]):
            r = myBoard.result(myBoard.board)
            print("Score is:", r)
            match r:
                case 10:
                    print("Bot won!")
                case -10:
                    print("You won!")
                case _:
                    print("Tie")
            
            break