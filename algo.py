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