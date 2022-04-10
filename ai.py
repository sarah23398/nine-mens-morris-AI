import copy
import math

# Max recursion depth: level 5

map = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
verticals = [[0, 9, 21], [3, 10, 18], [6, 11, 15], [1, 4, 7], [16, 19, 22], [8, 12, 17], [5, 13, 20], [2, 14, 23]]
scores = {}
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

def generate_moves(map, player):
    moves = []
    for i in range(len(map)):
        if map[i] == 'x':
            move = copy.deepcopy(map)
            move[i] = player
            moves.append(move)
    return moves

def minimax(map, level, player):
    if player == 1: best_score = -math.inf
    else: best_score = math.inf
    best_move = None

    if game_over or level == 0:
        best_score = evaluate(map, 1)
    else:
        children = generate_moves(map, player)
        if player == 1:
            for child in children:
                move = child
                if tuple(move) in scores:
                    score = scores[tuple(move)]
                else:
                    score = minimax(move, level - 1, 2)[0]
                    scores[tuple(move)] = score
                if score > best_score: 
                    best_score = score
                    best_move = move
        else:
            for child in children:
                move = child
                if tuple(move) in scores:
                    score = scores[tuple(move)]
                else:
                    score = minimax(move, level - 1, 1)[0]
                    scores[tuple(move)] = score
                if score < best_score: 
                    best_score = score
                    best_move = move
    return best_score, best_move

print(minimax(map, 5, 1))