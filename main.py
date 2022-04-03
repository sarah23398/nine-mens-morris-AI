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

#function called during player's turn during phase one, placing pieces
def phase1(map,move, player):
    if move > 23 or move < 0:
        print("Invalid input: out of range")
        print_map(map)
        move = input()
        phase1(map,move, player)
    elif(map[int(move)]!='x'):#the piece cannot be placed because a piece is already there
        print("Invalid input: position is taken.")
        print_map(map)
        move = input()
        phase1(map,move, player)
    else:
        print("Player " + str(player) + " made a move on "+move)
        map[int(move)] = player
        print_map(map)

#function called during player's turn during phase two, moving pieces
def phase2(map, org, des, player):
    if org > 23 or org < 0 or des > 23 or des < 0:
        print("Invalid input: out of range")
        print_map(map)
        org = input()
        des = input()
        phase1(map, org, des, player)
    elif (map[int(org)] != player) or (map[int(des) != 'x']):
        print("Invalid input")
        print_map(map)
        org = input()
        des = input()
        phase2(map, org, des, player)
    else:
        print("Player " + str(player) + " moved a piece from " + org + " to " + des)
        map[int(org)] = 'x'
        map[int(des)] = player
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
#can only remove if piece doesn't form a line
def remove_piece(map, move, player):
    if(map[move]==1 and player==2):
        if not in_line(map, move):
            print("Player 2 removed Player 1's piece at "+str(move))
            map[move] = 'x'
            print_map(map)
    elif(map[move]==2 and player==1):
        if not in_line(map, move):
            print("Player 1 removed Player 2's piece at "+str(move))
            map[move] = 'x'
            print_map(map)
    else:
        print("Invalid move")
        print_map(map)
        move = input()
        remove_piece(map, int(move), player)

#function to check if a specified piece forms a line
def in_line(map, move):
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
    phase1(map,move, 1)
    player1_moves-=1
    if(check_line(map,1)):
        print("Player 1 can remove a piece:")
        move = input()
        remove_piece(map,int(move),1)

    print("Player 2's turn:")
    move = input()
    phase1(map,move, 2)
    player2_moves-=1
    if(check_line(map,2)):
        print("Player 2 can remove a piece:")
        move = input()
        remove_piece(map,int(move),2)
print("Final map: ")
print_map(map)

while True:
    print("Phase 2:")
    print("Player 1's turn:")
    org = input()
    des = input()
    phase2(map, move, org, des, 1)
    if(check_line(map,1)):
        print("Player 1 can remove a piece:")
        move = input()
        remove_piece(map,int(move),1)

    print("Player 2's turn:")
    org = input()
    des = input()
    phase2(map, move, org, des, 2)
    if(check_line(map,2)):
        print("Player 2 can remove a piece:")
        move = input()
        remove_piece(map,int(move),2)
