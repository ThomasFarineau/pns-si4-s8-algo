import math
import random

score_heuristics = [[2, 2, 2, 2, 2, 2], [3, 4, 5, 5, 4, 3], [4, 6, 8, 8, 6, 4], [6, 8, 10, 10, 8, 6],
                    [4, 6, 8, 8, 6, 4], [3, 4, 5, 5, 4, 3], [2, 2, 2, 2, 2, 2]]
grid = ""
currentPlayer = ""
time = 2
MIN_VALUE = -100000
MAX_VALUE = 100000


def next_move(last_move):
    # time = perfomance.now()
    play(grid, last_move[0], last_move[1], currentPlayer)
    if last_move.length != 0:
        if currentPlayer == 'm':
            currentPlayer = 'h'
        elif currentPlayer == 'h':
            currentPlayer = 'm'
    ret = 0
    finalRet = 0
    depth = 1
    while depth <= 42:  # time should be checked
        finalRet = ret
        ret = minimax(grid, currentPlayer, depth, MIN_VALUE, MAX_VALUE)[1]
        depth += 1
    if (finalRet[0] == -1) and (finalRet[1] == -1):
        finalRet = playableMoves(grid)[random.randint(0, 7)]
    play(grid, finalRet[0], finalRet[1], currentPlayer)

    if currentPlayer == 1:
        currentPlayer = 2
    elif currentPlayer == 2:
        currentPlayer = 1
    return finalRet


def play(gr, col, row, player):
    n = 0
    for e in gr[col]:
        if e == 0:
            n += 1

    if n > 0:
        gr[col][6 - n] = player
        return True


def minimax(gameState, player, depth, alpha, beta):
    if (100 - time) > 98:
        val = 0
        if player == 1:
            val = MIN_VALUE
        if player == 2:
            val = MAX_VALUE
        return [val, [-1, -1]]

    allMoves = playableMoves(gameState)
    score = applyPoints(gameState)

    if depth == 0 or score <= -1000 or score >= 1000 or len(allMoves) == 0:
        return [score, [-1, -1]]

    if player == 1:
        moveToPlay = [-1, -1]
        maxVal = MIN_VALUE
        for element in allMoves:
            currentMove = element
            newGameState = []
            for j in range(7):
                c = []
                for k in range(6):
                    c[k] = (gameState[j][k] * 1)
                newGameState[j] = c
            play(newGameState, currentMove[0], currentMove[1], 1)
            val = minimax(newGameState, 2, depth - 1, alpha, beta)[0]
            if val > maxVal:
                maxVal = val
                moveToPlay = currentMove
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return [maxVal, moveToPlay]
    if player == 2:
        moveToPlay = [-1, -1]
        minVal = MAX_VALUE
        for element in allMoves:
            currentMove = element
            newGameState = []
            for j in range(7):
                c = []
                for k in range(6):
                    c[k] = (gameState[j][k] * 1)
                newGameState[j] = c
            play(newGameState, currentMove[0], currentMove[1], 2)
            val = minimax(newGameState, 1, depth - 1, alpha, beta)[0]
            if val < minVal:
                minVal = val
                moveToPlay = currentMove
            beta = min(beta, val)
            if beta <= alpha:
                break
        return [minVal, moveToPlay]


def ScoreHeuristic(HumanInRow, ComputerInRow, p1Tokens, p2Tokens):
    points = 0
    if HumanInRow == 4:
        points += 100000
    elif HumanInRow == 3:
        if p2Tokens == 0:
            points += 80
        else:
            points += 40
    elif HumanInRow == 2:
        points += 20 - 5 * p2Tokens

    if ComputerInRow == 4:
        points -= 100000
    elif ComputerInRow == 3:
        if p1Tokens == 0:
            points -= 80
        else:
            points -= 40
    elif ComputerInRow == 2:
        points -= 20 + 5 * p1Tokens
    return points


def applyPoints(gameState):
    score = 0
    for i in range(0, 7):
        for j in range(0, 6):
            if gameState[i][j] == 'm':
                # print("+", score_heuristics[i][j])
                score += score_heuristics[i][j]
            elif gameState[i][j] == 'h':
                # print("-", score_heuristics[i][j])
                score -= score_heuristics[i][j]
    # apply points for rows
    for rows in range(6):
        for column in range(7 - 4):
            p1InRow = 0
            p2InRow = 0
            p1Tokens = 0
            p2Tokens = 0
            for offset in range(column, column + 4):
                if gameState[offset][rows] == 1:
                    p1InRow += 1
                    p2InRow = 0
                    p1Tokens += 1
                elif gameState[offset][rows] == 2:
                    p2InRow += 1
                    p1InRow = 0
                    p2Tokens += 1

            score += ScoreHeuristic(p1InRow, p2InRow, p1Tokens, p2Tokens)
            if score <= -1000 or score >= 1000:
                return score

    # apply points for columns
    for column in range(7):
        for rows in range(6 - 4):
            p1InRow = 0
            p2InRow = 0
            p1Tokens = 0
            p2Tokens = 0
            for offset in range(rows, rows + 4):
                if gameState[column][offset] == 1:
                    p1InRow += 1
                    p2InRow = 0
                    p1Tokens += 1
                elif gameState[column][offset] == 2:
                    p2InRow += 1
                    p1InRow = 0
                    p2Tokens += 1

            score += ScoreHeuristic(p1InRow, p2InRow, p1Tokens, p2Tokens)
            if score <= -1000 or score >= 1000:
                return score

    # apply points for diag
    for column in range(7 - 4):
        for rows in range(6 - 4):
            p1InRow = 0
            p2InRow = 0
            p1Tokens = 0
            p2Tokens = 0
            for offset in range(rows, rows + 4):
                if gameState[column + (offset - rows)][offset] == 1:
                    p1InRow += 1
                    p2InRow = 0
                    p1Tokens += 1
                elif gameState[column + (offset - rows)][offset] == 2:
                    p2InRow += 1
                    p1InRow = 0
                    p2Tokens += 1

            score += ScoreHeuristic(p1InRow, p2InRow, p1Tokens, p2Tokens)
            if score <= -1000 or score >= 1000:
                return score

    # apply points for anti diag
    for column in reversed(range(7 - 1, 7 - 4)):
        for rows in range(6 - 4):
            p1InRow = 0
            p2InRow = 0
            p1Tokens = 0
            p2Tokens = 0
            for offset in range(rows, rows + 4):
                if gameState[column - (offset - rows)][offset] == 1:
                    p1InRow += 1
                    p2InRow = 0
                    p1Tokens += 1
                elif gameState[column - (offset - rows)][offset] == 2:
                    p2InRow += 1
                    p1InRow = 0
                    p2Tokens += 1

            score += ScoreHeuristic(p1InRow, p2InRow, p1Tokens, p2Tokens)
            if score <= -1000 or score >= 1000:
                return score
    return score


def playableMoves(gameState):
    ret = []
    for i in range(7):
        for j in range(6):
            if (gameState[i][j] == None):
                ret.append([i, j])
                break
    return ret
