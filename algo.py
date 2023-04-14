import math
import time

position_heuristics = [[2, 2, 2, 2, 2, 2], [3, 4, 5, 5, 4, 3], [4, 6, 8, 8, 6, 4], [6, 8, 10, 10, 8, 6],
                       [4, 6, 8, 8, 6, 4], [3, 4, 5, 5, 4, 3], [2, 2, 2, 2, 2, 2], ]


def play_move(grid, move, player):
    grid[move[0]][move[1]] = player
    return grid, move[0], move[1]


def playable_row(row):
    for r in range(5, -1, -1):
        if row[r] is None:
            return r
    return None


def score_heuristique(in_row, tokens):
    points = 0
    if in_row[0] == 4:
        points += 100000
    elif in_row[0] == 3:
        if tokens[1] == 0:
            points += 80
        else:
            points += 40
    elif in_row[0] == 2:
        points += 20 - 5 * tokens[1]
    if in_row[1] == 4:
        points -= 100000
    elif in_row[1] == 3:
        if tokens[0] == 0:
            points -= 80
        else:
            points -= 40
    elif in_row[1] == 2:
        points -= 20 - 5 * tokens[0]
    return points


def possible_moves(grid):
    moves = []
    for c in range(7):
        if playable_row(grid[c]) is not None:
            moves.append([c, playable_row(grid[c])])
    return moves


def eval_board(grid):
    score = 0
    for c in range(7):
        for r in range(6):
            if grid[c][r] == 'm':
                score += position_heuristics[c][r]
            elif grid[c][r] == 'h':
                score -= position_heuristics[c][r]
    # apply points for each row
    for r in range(6):
        for c in range(7 - 4):
            in_row = [0, 0]
            tokens = [0, 0]
            for o in range(c, c + 4):
                if grid[o][r] == 'm':
                    in_row[0] += 1
                    in_row[1] = 0
                    tokens[0] += 1
                elif grid[o][r] == 'h':
                    in_row[1] += 1
                    in_row[0] = 0
                    tokens[1] += 1
            score += score_heuristique(in_row, tokens)
            if score <= -1000 or score >= 1000:
                return score
    # apply points for each column
    for c in range(7):
        for r in range(6 - 4):
            in_row = [0, 0]
            tokens = [0, 0]
            for o in range(r, r + 4):
                if grid[c][o] == 'm':
                    in_row[0] += 1
                    in_row[1] = 0
                    tokens[0] += 1
                elif grid[c][o] == 'h':
                    in_row[1] += 1
                    in_row[0] = 0
                    tokens[1] += 1
            score += score_heuristique(in_row, tokens)
            if score <= -1000 or score >= 1000:
                return score
    # apply points for each diagonal
    for c in range(7 - 4):
        for r in range(6 - 4):
            in_row = [0, 0]
            tokens = [0, 0]
            for o in range(r, r + 4):
                if grid[c + (o - r)][o] == 'm':
                    in_row[0] += 1
                    in_row[1] = 0
                    tokens[0] += 1
                elif grid[c + (o - r)][o] == 'h':
                    in_row[1] += 1
                    in_row[0] = 0
                    tokens[1] += 1
            score += score_heuristique(in_row, tokens)
            if score <= -1000 or score >= 1000:
                return score
    # apply points for each anti-diagonal
    for c in range(7 - 1, 7 - 4):
        for r in range(6 - 4):
            in_row = [0, 0]
            tokens = [0, 0]
            for o in range(r, r + 4):
                if grid[c - (o - r)][o] == 'm':
                    in_row[0] += 1
                    in_row[1] = 0
                    tokens[0] += 1
                elif grid[c - (o - r)][o] == 'h':
                    in_row[1] += 1
                    in_row[0] = 0
                    tokens[1] += 1
            score += score_heuristique(in_row, tokens)
            if score <= -1000 or score >= 1000:
                return score
    return score


def minimax(grid, depth, alpha, beta, maximizing_player):
    moves = possible_moves(grid)
    score = eval_board(grid)
    if depth == 0 or score <= -1000 or score >= 1000 or len(moves) == 0:
        return score, None
    if maximizing_player:
        max_val, best_move = -math.inf, None
        for move in moves:
            new_grid, row, _ = play_move([row.copy() for row in grid], move, 'm')
            val, _ = minimax(new_grid, depth - 1, alpha, beta, False)
            if val > max_val:
                max_val = val
                best_move = move
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_val, best_move
    else:
        min_val, best_move = math.inf, None
        for move in moves:
            new_grid, row, _ = play_move([row.copy() for row in grid], move, 'h')
            val, _ = minimax(new_grid, depth - 1, alpha, beta, True)
            if val < min_val:
                min_val = val
                best_move = move
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_val, best_move


def best_move(grid, max_time):
    # set the current time to now
    start_time = time.time()
    print("start time: ", start_time)
    move, final_move = None, None
    depth = 1
    while time.time() - start_time < max_time and depth <= 42:
        final_move = move
        _, move = minimax(grid, depth, -math.inf, math.inf, True)
        depth += 1
    print("[DEBUG] depth: ", depth)
    return [final_move[0] + 1, final_move[1] + 1]
