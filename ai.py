import copy
import math
from main import in_line

# Max recursion depth: level 5

map = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
verticals = [[0, 9, 21], [3, 10, 18], [6, 11, 15], [1, 4, 7], [16, 19, 22], [8, 12, 17], [5, 13, 20], [2, 14, 23]]
scores1 = {}
scores2 = {}
game_over = False

# Scores are as follows:
# Player's full mills: 100
# Opponent's full mills: -100
# Player's half mills: 10
# Opponent's half mills: -10
# Player's piece: 1 per free space in all directions
                # 50 if blocking opponent's mill
# Opponent's piece: -1 per free space in all directions
                # -50 is blocking player's mill

def mill_score(map):
    score = 0
    for i in range(0, 21, 3):
        if map[i] == 1 and map[i + 1] == 1 and map[i + 2] == 1:
            score += 100

    for v in verticals:
        if map[v[0]] == 1 and map[v[1]] == 1 and map[v[2]] == 1:
            score += 100
        
    for i in range(0, 21, 3):
        if map[i] == 2 and map[i + 1] == 2 and map[i + 2] == 2:
            score -= 100

    for v in verticals:
        if map[v[0]] == 2 and map[v[1]] == 2 and map[v[2]] == 2:
            score -= 100
    
    return score

def setup_mill_score(map):
    score = 0
    for i in range(0, 21, 3):
        if map[i] == 1 and map[i + 1] == 1:
            if map[i + 2] == 'x':
                score += 10
        elif map[i] == 1 and map[i + 2] == 1:
            if map[i + 1] == 'x':
                score += 10
        elif map[i + 1] == 1 and map[i + 2] == 1:
            if map[i] == 'x':
                score += 10
        elif map[i] == 1 or map[i + 1] == 1 or map[i + 2] == 1:
            for j in range(i, i + 3):
                if map[j] == 'x':
                    score += 1

    for v in verticals:
        if map[v[0]] == 1 and map[v[1]] == 1:
            if map[v[2]] == 'x':
                score += 10
        elif map[v[0]] == 1 and map[v[2]] == 1:
            if map[v[1]] == 'x':
                score += 10
        elif map[v[1]] == 1 and map[v[2]] == 1:
            if map[v[0]] == 'x':
                score += 10
        elif map[v[1]] == 1 or map[v[1]] == 1 or map[v[2]] == 1:
            for j in range(3):
                if map[v[j]] == 'x':
                    score += 1
        
    for i in range(0, 21, 3):
        if map[i] == 1 and map[i + 1] == 1:
            if map[i + 2] == 'x':
                score -= 10
        elif map[i] == 1 and map[i + 2] == 1:
            if map[i + 1] == 'x':
                score -= 10
        elif map[i + 1] == 1 and map[i + 2] == 1:
            if map[i] == 'x':
                score -= 10
        elif map[i] == 1 or map[i + 1] == 1 or map[i + 2] == 1:
            for j in range(i, i + 3):
                if map[j] == 'x':
                    score -= 1

    for v in verticals:
        if map[v[0]] == 1 and map[v[1]] == 1:
            if map[v[2]] == 'x':
                score -= 10
        elif map[v[0]] == 1 and map[v[2]] == 1:
            if map[v[1]] == 'x':
                score -= 10
        elif map[v[1]] == 1 and map[v[2]] == 1:
            if map[v[0]] == 'x':
                score -= 10
        elif map[v[1]] == 1 or map[v[1]] == 1 or map[v[2]] == 1:
            for j in range(3):
                if map[v[j]] == 'x':
                    score -= 1
    
    return score

def block_score(map):
    score = 0
    for i in range(0, 21, 3):
        if map[i] == 2 and map[i + 1] == 2:
            if map[i + 2] == 1:
                score += 50
        elif map[i] == 2 and map[i + 2] == 2:
            if map[i + 1] == 1:
                score += 50
        elif map[i + 1] == 2 and map[i + 2] == 2:
            if map[i] == 1:
                score += 50

    for v in verticals:
        if map[v[0]] == 2 and map[v[1]] == 2:
            if map[v[2]] == 1:
                score += 50
        elif map[v[0]] == 2 and map[v[2]] == 2:
            if map[v[1]] == 1:
                score += 50
        elif map[v[1]] == 2 and map[v[2]] == 2:
            if map[v[0]] == 1:
                score += 50
    
    for i in range(0, 21, 3):
        if map[i] == 1 and map[i + 1] == 1:
            if map[i + 2] == 2:
                score -= 50
        elif map[i] == 1 and map[i + 2] == 1:
            if map[i + 1] == 2:
                score -= 50
        elif map[i + 1] == 1 and map[i + 2] == 1:
            if map[i] == 2:
                score -= 50

    for v in verticals:
        if map[v[0]] == 1 and map[v[1]] == 1:
            if map[v[2]] == 2:
                score -= 50
        elif map[v[0]] == 1 and map[v[2]] == 1:
            if map[v[1]] == 2:
                score -= 50
        elif map[v[1]] == 1 and map[v[2]] == 1:
            if map[v[0]] == 2:
                score -= 50

    return score


def evaluate(map, phase):
    mill = mill_score(map)
    setup_mill = setup_mill_score(map)
    block = block_score(map)

    score = mill + setup_mill + block
    
    return score

# Phase 0 = removal
def generate_moves(map, player, phase):
    moves = []
    for i in range(len(map)):
        if phase == 0:
            if map[i] == abs(player - 1):
                move = (None, i)
                moves.append(move)
        elif phase == 1:
            if map[i] == 'x':
                move = (i, None)
                moves.append(move)
        elif phase == 2:
            pass
        else:
            pass
    return moves


def minimax(map, level, player, phase, remove):
    if player == 1: best_score = -math.inf
    else: best_score = math.inf
    best_move = None

    if game_over or level == 0:
        best_score = evaluate(map, 1)
    else:
        if remove: children = generate_moves(map, player, 0)
        else: children = generate_moves(map, player, phase)
        remove = False
        if player == 1:
            for child in children:
                move = child
                if move in scores1:
                    score = scores1[move]
                else:
                    new_map = copy.deepcopy(map)
                    if move[0] != None:
                        new_map[move[0]] = 'x'
                    if move[1] != None:
                        new_map[move[1]] = player
                        if in_line(new_map, move[1]):
                            remove = True
                    score = minimax(new_map, level - 1, 2, phase, remove)[0]
                    scores1[move] = score
                if score > best_score: 
                    best_score = score
                    best_move = move
        else:
            for child in children:
                move = child
                if move in scores2:
                    score = scores2[move]
                else:
                    new_map = copy.deepcopy(map)
                    if move[0] != None:
                        new_map[move[0]] = 'x'
                    if move[1] != None:
                        new_map[move[1]] = player
                        if in_line(new_map, move[1]):
                            remove = True
                    score = minimax(new_map, level - 1, 1, phase, remove)[0]
                    scores2[move] = score
                if score < best_score: 
                    best_score = score
                    best_move = move
    return best_score, best_move

print(minimax(map, 10, 1, 1, False))