# Code inspired by: https://www3.ntu.edu.sg/home/ehchua/programming/java/javagame_tictactoe_ai.html

import copy
import math

# Max recursion depth: level 5

map = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
verticals = [[0, 9, 21], [3, 10, 18], [6, 11, 15], [1, 4, 7], [16, 19, 22], [8, 12, 17], [5, 13, 20], [2, 14, 23]]
scores = {}
game_over = False

def evaluate(map):
    score = 0
    for i in range(0, 21, 3):
        if map[i] == 1 and map[i + 1] == 1 and map[i + 2] == 1:
            score += 100
        elif (map[i] == 1 and map[i + 1] == 1) or (map[i] == 1 and map[i + 2] == 1) or (map[i + 1] == 1 and map[i + 2] == 1):
            score += 10
        elif map[i] == 1 or map[i + 1] == 1 or map[i + 2] == 1:
            score += 1

    for v in verticals:
        if map[v[0]] == 1 and map[v[1]] == 1 and map[v[2]] == 1:
            score += 100
        elif (map[v[0]] == 1 and map[v[1]] == 1) or (map[v[0]] == 1 and map[v[2]] == 1) or (map[v[1]] == 1 and map[v[2]] == 1):
            score += 10
        elif map[v[0]] == 1 or map[v[1]] == 1 or map[v[2]] == 1:
            score += 1
        
    for i in range(0, 21, 3):
        if map[i] == 2 and map[i + 1] == 2 and map[i + 2] == 2:
            score -= 100
        elif (map[i] == 2 and map[i + 1] == 2) or (map[i] == 2 and map[i + 2] == 2) or (map[i + 1] == 2 and map[i + 2] == 2):
            score -= 10
        elif map[i] == 2 or map[i + 1] == 2 or map[i + 2] == 2:
            score -= 1

    for v in verticals:
        if map[v[0]] == 2 and map[v[1]] == 2 and map[v[2]] == 2:
            score -= 100
        elif (map[v[0]] == 2 and map[v[1]] == 2) or (map[v[0]] == 2 and map[v[2]] == 2) or (map[v[1]] == 2 and map[v[2]] == 2):
            score -= 10
        elif map[v[0]] == 2 or map[v[1]] == 2 or map[v[2]] == 2:
            score -= 1
    
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
        best_score = evaluate(map)
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

print(minimax(map, 6, 1))