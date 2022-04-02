import math

#function for printing the current state of the board, takes a double array as input for the map
#empty spots are represented by 0, player 1 and 2's pieces are represented by 1 and 2
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
def player1_turn1(map,move):
    if(map[int(move)]!=0):#the piece cannot be placed because a piece is already there
        print("invalid input")
        print_map(map)
        move = input()
        player1_turn1(map,move)
    else:
        print("player 1 made a move on "+move)
        map[int(move)] = 1
        print_map(map)

def player2_turn1(map,move):
    if(map[int(move)]!=0):
        print("invalid input")
        print_map(map)
        move = input()
        player2_turn1(map,move)
    else:
        print("player 2 made a move on "+move)
        map[int(move)] = 2
        print_map(map)

#function to check if the specified player has a line on the board
def check_line(map,player):
    line = False
    if(map[0]==player and map[1]==player and map[2]==1):
        line = True
    if(map[3]==player and map[4]==player and map[5]==player):
        line = True
    if(map[6]==player and map[7]==player and map[8]==player):
        line = True
    if(map[9]==player and map[10]==player and map[11]==player):
        line = True
    if(map[12]==player and map[13]==player and map[14]==player):
        line = True
    if(map[15]==player and map[16]==player and map[17]==player):
        line = True
    if(map[18]==player and map[19]==player and map[20]==player):
        line = True
    if(map[21]==player and map[22]==player and map[23]==player):
        line = True

    if(map[0]==player and map[9]==player and map[21]==player):
        line = True
    if(map[3]==player and map[10]==player and map[18]==player):
        line = True
    if(map[6]==player and map[11]==player and map[15]==player):
        line = True
    if(map[1]==player and map[4]==player and map[7]==player):
        line = True
    if(map[16]==player and map[19]==player and map[22]==player):
        line = True
    if(map[8]==player and map[12]==player and map[17]==player):
        line = True
    if(map[5]==player and map[13]==player and map[20]==player):
        line = True
    if(map[3]==player and map[15]==player and map[23]==player):
        line = True
    return line

#function for a specified player to remove their opponent's piece
def remove_piece(map, move, player):
    if(map[move]==1 and player==2):
        print("player 2 removed player 1's piece at "+str(move))
        map[move] = 0
        print_map(map)
    elif(map[move]==2 and player==1):
        print("player 1 removed player 2's piece at "+str(move))
        map[move] = 0
        print_map(map)
    else:
        print("invalid move")
        print_map(map)
        move = input()
        remove_piece(map, int(move), player)

#function to check if a specified piece forms a line
def make_line(map, move):
    if(map[move]==0)return False
    remove = True
    if(move==0 or move==1 or move==2):
        if(map[0]==map[1] and map[1]==map[2]):
            remove = False
    if(move==3 or move==4 or move==5):
        if(map[3]==map[4] and map[4]==map[5]):
            remove = False
    if(move==6 or move==7 or move==8):
        if(map[6]==map[7] and map[7]==map[8]):
            remove = False
    if(move==9 or move==10 or move==11):
        if(map[9]==map[10] and map[10]==map[11]):
            remove = False
    if(move==12 or move==13 or move==14):
        if(map[12]==map[13] and map[13]==map[14]):
            remove = False
    if(move==15 or move==16 or move==17):
        if(map[15]==map[16] and map[16]==map[17]):
            remove = False
    if(move==18 or move==19 or move==20):
        if(map[18]==map[19] and map[19]==map[20]):
            remove = False
    if(move==21 or move==22 or move==23):
        if(map[21]==map[22] and map[22]==map[23]):
            remove = False

    if(move==0 or move==9 or move==21):
        if(map[0]==map[9] and map[9]==map[21]):
            remove = False
    if(move==3 or move==10 or move==18):
        if(map[3]==map[10] and map[10]==map[18]):
            remove = False
    if(move==6 or move==11 or move==15):
        if(map[6]==map[11] and map[11]==map[15]):
            remove = False
    if(move==1 or move==4 or move==7):
        if(map[1]==map[4] and map[4]==map[7]):
            remove = False
    if(move==16 or move==19 or move==22):
        if(map[16]==map[19] and map[19]==map[22]):
            remove = False
    if(move==8 or move==12 or move==17):
        if(map[8]==map[12] and map[12]==map[17]):
            remove = False
    if(move==5 or move==13 or move==20):
        if(map[5]==map[13] and map[13]==map[20]):
            remove = False
    if(move==3 or move==15 or move==23):
        if(map[3]==map[15] and map[15]==map[23]):
            remove = False
    return not remove

map = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

player1_moves = 9
player2_moves = 9
while(player1_moves!=0 and player2_moves!=0):
    print("it is player 1's turn")
    move = input()
    player1_turn1(map,move)
    player1_moves-=1
    if(check_line(map,1)):
        print("player 1 can remove a piece")
        move = input()
        remove_piece(map,int(move),1)

    print("it is player 2's turn")
    move = input()
    player2_turn1(map,move)
    player2_moves-=1
    if(check_line(map,2)):
        print("player 2 can remove a piece")
        move = input()
        remove_piece(map,int(move),2)
print("final map: ")
print_map(map)
