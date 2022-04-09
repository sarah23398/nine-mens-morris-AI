import math

board = [[0,0,0,0,0,1,0,0],[0,0,2,2,2,1,2,2],[0,0,1,1,1,0,0,2]]#white1, black2

def next_to(ring, piece):#return an array where each element is a neighbouring node represented by [ring, piece]
    if(piece%2==0):#a corner
        return [[ring, (piece+1)%8],[ring, (piece-1)%8]]
    else:
        if(ring==1):#middle piece on middle ring
            return [[ring, (piece+1)%8],[ring, (piece-1)%8],[ring-1, piece],[ring+1, piece]]
        elif(ring==0):#outer ring
            return [[ring, (piece+1)%8],[ring, (piece-1)%8], [ring+1, piece]]
        else:#inner ring
            return [[ring, (piece+1)%8],[ring, (piece-1)%8], [ring-1, piece]]

def mill_neighbours(ring, piece):#return an array of size 2, each element containing 2 pieces that could form a mill with the specified piece
    if(piece%2==0):#a corner
        return [[[ring, (piece+1)%8], [ring, (piece+2)%8]], [[ring, (piece-1)%8],[ring, (piece-2)%8]]]
    else:
        return [[[ring, (piece+1)%8], [ring, (piece-1)%8]], [[(ring+1)%3, piece],[(ring-1)%3, piece]]] #first is in same ring, second is in diff rings


def breath_alg(board, player): #returns how much breath a player holds, idea taken from go
    breath_score = 0
    for ring in range(3):
        for piece in range(8):
            if(board[ring][piece]==player):
                for neighbour in next_to(ring, piece):
                    if (board[neighbour[0]][neighbour[1]]==0):
                        breath_score += 1
    return breath_score

def mill_alg(board, player):#returns scores based on mills formed/being formed. full mill is worth 100, half mill is worth 10, if the mill is blocked it is worth 0
    mill_score = 0
    mill_total = 0
    mill_partial = 0
    for ring in range(3):
        for piece in range(8):
            if(board[ring][piece]==player):
                mills = mill_neighbours(ring,piece)
                mill1_score = 0
                mill2_score = 0
                for neighbour in mills[0]:#count how many pieces are in the mill(at least one already)
                    if(board[neighbour[0]][neighbour[1]]==player):
                        mill1_score += 1
                    elif(board[neighbour[0]][neighbour[1]]!=0):#if mill is blocked
                        mill1_score -= 10
                for neighbour in mills[1]:#count how many pieces are in the mill(at least one already)
                    if(board[neighbour[0]][neighbour[1]]==player):
                        mill2_score += 1
                    elif(board[neighbour[0]][neighbour[1]]!=0):#if mill is blocked
                        mill2_score -= 10

                if mill1_score==2:
                    mill_total+=100
                elif mill1_score==1:
                    mill_partial+=10

                if mill2_score==2:
                    mill_total+=100
                elif mill2_score==1:
                    mill_partial+=10

    mill_total/=3
    mill_partial/=2
    mill_score = mill_total+mill_partial
    return mill_score

def placing_alg(board, player):
    return breath_alg(board, player) + mill_alg(board,player)

def removing_alg(board, player):#same algorithm but for other player to find best piece to remove
    return placing_alg(board, 3-player)

def moving_alg(board1, board2, player):#board1 is the initial state, board2 is the state after the piece as been moved
    return placing_alg(board2, player)-placing_alg(board1,player)

def flying_alg(board1, board2, player):
    return placing_alg(board2, player)-placing_alg(board1,player)
