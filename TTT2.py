#tic tac toe with minimax algorithm
import os
import time
board = [list("-")*3,list("-")*3,list("-")*3]

def print_board():
   print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
   print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
   print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def take_turn(player, row=None, column=None):
    print(player + "'s turn.")
    if player == human:
        row = input("choose a position from ROW: 0-2: ")
        column = input("choose a position from COL: 0-2: ")
        ##row = row
        ##column = column
    # while row not in [str(i) for i in range(0, 2)] or column not in [str(i) for i in range(0, 2)]:
    #     row = input("invalid input. Chose a position from  ROW 0-2: ")
    #     column = input("invalid input. Chose a position from COL 0-2: ")

    row = int(row)
    column = int(column)
    while board[row][column] != "-":
        row = int(input("Position already taken. Choose a different row: "))
        column = int(input("Position already taken. Choose a different column: "))
    board[row][column] = player
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board()

def check_game_over():
    if (board[0][0] == board[0][1] == board[0][2] != "-") or \
       (board[1][0] == board[1][1] == board[1][2] != "-") or \
       (board[2][0] == board[2][1] == board[2][2] != "-") or \
       (board[0][0] == board[1][0] == board[2][0] != "-") or \
       (board[0][1] == board[1][1] == board[2][1] != "-") or \
       (board[0][2] == board[1][2] == board[2][2] != "-") or \
       (board[0][0] == board[1][1] == board[2][2] != "-") or \
       (board[0][2] == board[1][1] == board[2][0] != "-"):
        return "win"
    elif "-" not in board[0] and\
    "-" not in board[1] and \
    "-" not in board[2]:
        print(board)
        return "tie"

    else:
        return "play"



ai, human = 'X', 'O'


# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '-'):
                return True
    return False


# This is the evaluation function as discussed
# in the previous article ( http://goo.gl/sJgv68 )
def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == ai):
                return 1
            elif (b[row][0] == human):
                return -1

    # Checking for Columns for X or O victory.
    for col in range(3):

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

            if (b[0][col] == ai):
                return 1
            elif (b[0][col] == human):
                return -1

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

        if (b[0][0] == ai):
            return 1
        elif (b[0][0] == human):
            return -1

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

        if (b[0][2] == ai):
            return 1
        elif (b[0][2] == human):
            return -1

    # Else if none of them have won then return 0
    return 0


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax):
    score = evaluate(board)

    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 1):
        return score

    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -1):
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (isMovesLeft(board) == False):
        return 0

    # If this maximizer's move
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == '-'):
                    # Make the move
                    board[i][j] = ai

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(board,
                                             depth + 1,
                                             not isMax))

                    # Undo the move
                    board[i][j] = '-'
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == '-'):
                    # Make the move
                    board[i][j] = human

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, isMax))

                    # Undo the move
                    board[i][j] = '-'
        return best

    # This will return the best possible move for the player


def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if (board[i][j] == '-'):

                # Make the move
                board[i][j] = ai

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False)

                # Undo the move
                board[i][j] = '-'

                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    #print("The value of the best Move is :", bestVal)
    #print()
    return bestMove


# Driver code
# board = [
#     ['X', 'O', 'X'],
#     ['O', 'O', 'X'],
#     ['-', '-', '-']
# ]

# bestMove = findBestMove(board)
#
# print("The Optimal Move is :")
# print("ROW:", bestMove[0], " COL:", bestMove[1])
#

def play_game():
    print_board()
    current_player = ai
    game_over = False
    while not game_over:
        time.sleep(1)
        best_move = findBestMove(board)
        print(best_move)
        take_turn(current_player, best_move[0], best_move[1])
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = human if current_player == ai else ai

play_game()