import math
import random
score_heuristics = [[2, 2, 2, 2, 2, 2], [3, 4, 5, 5, 4, 3], [4, 6, 8, 8, 6, 4], [6, 8, 10, 10, 8, 6], [4, 6, 8, 8, 6, 4], [3, 4, 5, 5, 4, 3], [2, 2, 2, 2, 2, 2]]

def score(board):
    score = 0
    for i in range(0,7):
        for j in range(0,6):
            if (board[i][j] == 'm'):
                #print("+", score_heuristics[i][j])
                score += score_heuristics[i][j]
            elif (board[i][j] == 'h'):
                #print("-", score_heuristics[i][j])
                score -= score_heuristics[i][j]
    return score




def next_move(last_move):
    #time = perfomance.now();
    play(grid, last_move[0], last_move[1], currentPlayer)
    if (last_move.length != 0):
        if (currentPlayer == 'm'):
            currentPlayer = 'h'
        elif (currentPlayer == 'h'):
            currentPlayer = 'm'
    ret
    finalRet
    depth = 1
    while(depth <= 42):  # time should be checked
        finalRet = ret
        ret = minimax(grid, currentPlayer, -100000, 100000, currentPlayer)[1]
        depth += 1
    if (finalRet[0] == -1 and finalRet[1] == -1):
        finalRet = playableMoves(grid)[random.randint(0, 7)]