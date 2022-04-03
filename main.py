import math

#function for printing the current state of the board, takes a double array as input for the map
#empty spots are represented by x, player 1 and 2's pieces are represented by 1 and 2
def print_map(map):    
    print(str(map[0])+"-----"+str(map[1])+"-----"+str(map[2]))
    print("|     |     |")
    print("| "+str(map[3])+"---"+str(map[4])+"---"+str(map[5])+" |")
    print("| |   |   | |")

    print("| | "+str(map[6])+"-"+str(map[7])+"-"+str(map[8])+" | |")

    print("| | |   | | |")

    print(str(map[9])+"-"+str(map[10])+"-"+str(map[11])+"   "+str(map[12])+"-"+str(map[13])+"-"+str(map[14]))
    print("| | |   | | |")
    print("| | "+str(map[15])+"-"+str(map[16])+"-"+str(map[17])+" | |")
    print("| |   |   | |")
    print("| "+str(map[18])+"---"+str(map[19])+"---"+str(map[20])+" |")
    print("|     |     |")
    print(str(map[21])+"-----"+str(map[22])+"-----"+str(map[23]))

#function called during player1's turn during phase one, placing pieces
def player1_phase1(map,move):
    if(map[int(move)]!='x'):#the piece cannot be placed because a piece is already there
        print("Invalid input: position is taken.")
        print_map(map)
        move = input()
        player1_phase1(map,move)
    else:
        print("Player 1 made a move on "+move)
        map[int(move)] = 1
        print_map(map)

def player2_phase1(map,move):
    if(map[int(move)]!='x'):
        print("Invalid input: position is taken.")
        print_map(map)
        move = input()
        player2_phase1(map,move)
    else:
        print("Player 2 made a move on "+move)
        map[int(move)] = 2
        print_map(map)

#function to check if the specified player has a line on the board
verticals = [[0, 9, 21], [3, 10, 18], [6, 11, 15], [1, 4, 7], [16, 19, 22], [8, 12, 17], [5, 13, 20], [3, 15, 23]]
def check_line(map,player):
    line = False
    for i in range(0, 21, 3):
        if (map[i] == player and map[i + 1] == player and map[i + 2] == player):
            line = True
            break

    for v in verticals:
        if all(map[i] == player for i in v):
            line = True
            break

    return line

#function for a specified player to remove their opponent's piece
def remove_piece(map, move, player):
    if(map[move]==1 and player==2):
        print("Player 2 removed Player 1's piece at "+str(move))
        map[move] = 'x'
        print_map(map)
    elif(map[move]==2 and player==1):
        print("Player 1 removed Player 2's piece at "+str(move))
        map[move] = 'x'
        print_map(map)
    else:
        print("Invalid move")
        print_map(map)
        move = input()
        remove_piece(map, int(move), player)

#function to check if a specified piece forms a line
def make_line(map, move):
    if(map[move]=='x'): return False
    remove = True
    for i in range(0, 21, 3):
        if move == i or move == i + 1 or move == i + 2:
            if map[i] == map[i + 1] and map[i] == map[i + 2]:
                remove = False
                break

    for v in verticals:
        if move in v:
            if map[v[0]] == map[v[1]] and map[v[0]] == map[v[2]]:
                remove = False
                break
            
    return not remove

map = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']

player1_moves = 9
player2_moves = 9
while(player1_moves!=0 and player2_moves!=0):
    print("Player 1's turn:")
    move = input()
    player1_phase1(map,move)
    player1_moves-=1
    if(check_line(map,1)):
        print("Player 1 can remove a piece:")
        move = input()
        remove_piece(map,int(move),1)

    print("Player 2's turn:")
    move = input()
    player2_phase1(map,move)
    player2_moves-=1
    if(check_line(map,2)):
        print("Player 2 can remove a piece:")
        move = input()
        remove_piece(map,int(move),2)
print("Final map: ")
print_map(map)
