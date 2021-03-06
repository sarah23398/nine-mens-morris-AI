import math
from ai import minimax, in_line, verticals, rings, connectors

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
        phase1(map, int(move), player)
    elif(map[int(move)]!='x'):#the piece cannot be placed because a piece is already there
        print("Invalid input: position is taken.")
        print_map(map)
        move = input()
        phase1(map, int(move), player)
    else:
        print("Player " + str(player) + " made a move on "+ str(move))
        map[int(move)] = player
        count[player - 1] += 1
        print_map(map)

#function called during player's turn during phase two, moving pieces in a line
def phase2(map, org, des, player):
    can_move = False
    if org > 23 or org < 0 or des > 23 or des < 0:
        can_move = False
    elif(map[org]==player and map[des]=='x'):
        neighbours = next_to[org]
        if(des in neighbours):
            can_move = True
    if can_move: move(map, org, des, player)
    else:
        print("Invalid input: not moving in a line")
        print_map(map)
        org = input()
        des = input()
        phase2(map, org, des, player)

#function called during player's turn during phase three, moving pieces freely
def phase3(map, org, des, player):
    can_move = False
    if org > 23 or org < 0 or des > 23 or des < 0:
        can_move = False
    if(map[org]==player and map[des]=='x'):
        can_move = True
    if can_move: move(map, org, des, player)
    else:
        print("Invalid input: not moving in a line")
        print_map(map)
        org = input()
        des = input()
        phase3(map, org, des, player)

def move(map, org, des, player):
    print("Player " + str(player) + " moved a piece from " + str(org) + " to " + str(des))
    map[int(org)] = 'x'
    map[int(des)] = player
    print_map(map)

#function for a specified player to remove their opponent's piece
#can only remove if piece doesn't form a line
def remove_piece(map, move, player):
    if move > 23 or move < 0:
        print("Invalid input: out of bound.")
        move = input()
        remove_piece(map, int(move), player)
    elif(map[move]==1 and player==2):
        if not in_line(map, move):
            print("Player 2 removed Player 1's piece at "+str(move))
            map[move] = 'x'
            count[0] -= 1
            print_map(map)
        else:
            can_remove = True
            for piece in range(23):
                if(map[piece]==1 and piece!=move and not in_line(map,piece)):
                    can_remove = False
                    break
            if(can_remove):
                print("Player 2 removed Player 1's piece at "+str(move))
                map[move] = 'x'
                count[0] -= 1
                print_map(map)
            else:
                print("Invalid input: piece cannot be removed.")
                move = input()
                remove_piece(map, int(move), player)
    elif(map[move]==2 and player==1):
        if not in_line(map, move):
            print("Player 1 removed Player 2's piece at "+str(move))
            map[move] = 'x'
            count[1] -= 1
            print_map(map)
        else:
            can_remove = True
            for piece in range(23):
                if(map[piece]==2 and piece!=move and not in_line(map,piece)):
                    can_remove = False
                    break
            if(can_remove):
                print("Player 1 removed Player 2's piece at "+str(move))
                map[move] = 'x'
                count[1] -= 1
                print_map(map)
            else:
                print("Invalid input: piece cannot be removed.")
                move = input()
                remove_piece(map, int(move), player)
    else:
        print("Invalid move")
        print_map(map)
        move = input()
        remove_piece(map, int(move), player)

map = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
player1_moves = 9
player2_moves = 9
count = [0, 0]
next_to = [[1,9], [0,2,4], [1,14], [4,10], [1,3,5,7], [4,13], [7,11], [4,6,8], [7,12], [0,10,21], [3,9,11,8], [6,10,15], [8,13,17], [5,12,14,20], [2,13,23], [11,16], [15,17,19], [12,16], [10,19], [16,18,20,22], [13,19],[9,22],[19,21,23],[14,22]]

def play():
    global player1_moves
    global player2_moves
    while(player1_moves!=0 and player2_moves!=0):
        print("Player 1's turn:")
        move = minimax(map, 3, 1, 1, False)[1][1]
        phase1(map,int(move), 1)
        player1_moves-=1
        if(in_line(map, int(move))):
            print("Player 1 can remove a piece:")
            move = minimax(map, 3, 1, 1, True)[1][0]
            remove_piece(map,int(move),1)

        print("Player 2's turn:")
        move = input()
        phase1(map,int(move), 2)
        player2_moves-=1
        if(in_line(map, int(move))):
            print("Player 2 can remove a piece:")
            move = input()
            remove_piece(map,int(move),2)
    print("Final map: ")
    print_map(map)

    while count[0] > 2 and count[1] > 2:
        if count[0] > 3: player1_phase = 2
        else: player1_phase = 3
        if count[1] > 3: player2_phase = 2
        else: player2_phase = 3
        print("Player 1 in Phase " + str(player1_phase) + " and Player 2 in Phase " + str(player2_phase))

        print("Player 1's turn:")
        if player1_phase == 2:
            move = minimax(map, 5, 1, 2, False)[1]
            phase2(map, int(move[0]), int(move[1]), 1)
        else:
            move = minimax(map, 5, 1, 3, False)[1]
            phase3(map, int(move[0]), int(move[1]), 1)
        if(in_line(map, int(move[1]))):
            print("Player 1 can remove a piece:")
            move = minimax(map, 5, 1, 2, True)[1][0]
            remove_piece(map,int(move),1)

        print("Player 2's turn:")
        org = input()
        des = input()
        if player2_phase == 2:
            phase2(map, int(org), int(des), 2)
        else:
            phase3(map, int(org), int(des), 2)
        if(in_line(map, int(des))):
            print("Player 2 can remove a piece:")
            move = input()
            remove_piece(map,int(move),2)

    if count[0] == 2:
        print("Player 2 has won!")
    else:
        print("Player 1 has won!")

play()
