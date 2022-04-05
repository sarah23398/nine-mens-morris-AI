# Author: aqeelanwar
# Created: 12 March,2020, 7:06 PM
# Email: aqeel.anwar@gatech.edu

from tkinter import *
import numpy as np


player1_color = '#58ECB6'
player2_color = '#C834CA'
colors = ['#FFFFFF', '#58ECB6','#C834CA']
circles = [[55,95,280,320,505,545],[130,170,280,320,430,470],[205,245,280,320,355,395]]
class NMM_board():
    def __init__(self):
        self.window = Tk()
        self.window.title('Nine men\'s Morris')
        self.canvas=Canvas(self.window, width=600,height=600)
        self.canvas.pack()

        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

        self.current_turn = 1

        self.player_pieces = [0,0]

        self.phase = 1
        self.removal = False
        self.selected = [-1,-1]
        self.phase1_moves = 18
        self.finish = False


    def mainloop(self):
        self.window.mainloop()

    def update_draw(self):
        self.canvas.delete('all')
        if(self.removal):
            self.canvas.create_text(300, 30, font="cmr 25 bold", fill='black', text='player '+str(self.current_turn)+' removes a piece')
        else:
            self.canvas.create_text(300, 30, font="cmr 25 bold", fill='black', text='it is player '+str(self.current_turn)+'\'s turn')
        self.canvas.create_line(75, 75, 75, 525, width=2)
        self.canvas.create_line(75, 75, 525, 75, width=2)
        self.canvas.create_line(525, 75, 525, 525, width=2)
        self.canvas.create_line(75, 525, 525, 525, width=2)

        self.canvas.create_line(150, 150, 150, 450, width=2)
        self.canvas.create_line(150, 150, 450, 150, width=2)
        self.canvas.create_line(450, 450, 150, 450, width=2)
        self.canvas.create_line(450, 450, 450, 150, width=2)

        self.canvas.create_line(225, 225, 225, 375, width=2)
        self.canvas.create_line(225, 225, 375, 225, width=2)
        self.canvas.create_line(375, 375, 225, 375, width=2)
        self.canvas.create_line(375, 375, 375, 225, width=2)

        self.canvas.create_line(300, 75, 300, 225, width=2)
        self.canvas.create_line(525, 300, 375, 300, width=2)
        self.canvas.create_line(300, 525, 300, 375, width=2)
        self.canvas.create_line(75, 300, 225, 300, width=2)

        for i in range(3):
            self.canvas.create_oval(circles[i][0], circles[i][0], circles[i][1], circles[i][1], fill=colors[self.board[i][0]])
            self.canvas.create_oval(circles[i][2], circles[i][0], circles[i][3], circles[i][1], fill=colors[self.board[i][1]])
            self.canvas.create_oval(circles[i][4], circles[i][0], circles[i][5], circles[i][1], fill=colors[self.board[i][2]])
            self.canvas.create_oval(circles[i][4], circles[i][2], circles[i][5], circles[i][3], fill=colors[self.board[i][3]])
            self.canvas.create_oval(circles[i][4], circles[i][4], circles[i][5], circles[i][5], fill=colors[self.board[i][4]])
            self.canvas.create_oval(circles[i][2], circles[i][4], circles[i][3], circles[i][5], fill=colors[self.board[i][5]])
            self.canvas.create_oval(circles[i][0], circles[i][4], circles[i][1], circles[i][5], fill=colors[self.board[i][6]])
            self.canvas.create_oval(circles[i][0], circles[i][2], circles[i][1], circles[i][3], fill=colors[self.board[i][7]])

    def initialize_board(self):
        self.canvas.create_text(300, 30, font="cmr 25 bold", fill='black', text='it is player 1\'s turn')
        self.canvas.create_line(75, 75, 75, 525, width=2)
        self.canvas.create_line(75, 75, 525, 75, width=2)
        self.canvas.create_line(525, 75, 525, 525, width=2)
        self.canvas.create_line(75, 525, 525, 525, width=2)

        self.canvas.create_line(150, 150, 150, 450, width=2)
        self.canvas.create_line(150, 150, 450, 150, width=2)
        self.canvas.create_line(450, 450, 150, 450, width=2)
        self.canvas.create_line(450, 450, 450, 150, width=2)

        self.canvas.create_line(225, 225, 225, 375, width=2)
        self.canvas.create_line(225, 225, 375, 225, width=2)
        self.canvas.create_line(375, 375, 225, 375, width=2)
        self.canvas.create_line(375, 375, 375, 225, width=2)

        self.canvas.create_line(300, 75, 300, 225, width=2)
        self.canvas.create_line(525, 300, 375, 300, width=2)
        self.canvas.create_line(300, 525, 300, 375, width=2)
        self.canvas.create_line(75, 300, 225, 300, width=2)

        for i in range(3):
            self.canvas.create_oval(circles[i][0], circles[i][0], circles[i][1], circles[i][1], fill=colors[0])
            self.canvas.create_oval(circles[i][2], circles[i][0], circles[i][3], circles[i][1], fill=colors[0])
            self.canvas.create_oval(circles[i][4], circles[i][0], circles[i][5], circles[i][1], fill=colors[0])
            self.canvas.create_oval(circles[i][4], circles[i][2], circles[i][5], circles[i][3], fill=colors[0])
            self.canvas.create_oval(circles[i][4], circles[i][4], circles[i][5], circles[i][5], fill=colors[0])
            self.canvas.create_oval(circles[i][2], circles[i][4], circles[i][3], circles[i][5], fill=colors[0])
            self.canvas.create_oval(circles[i][0], circles[i][4], circles[i][1], circles[i][5], fill=colors[0])
            self.canvas.create_oval(circles[i][0], circles[i][2], circles[i][1], circles[i][3], fill=colors[0])

    def click_to_cord(self,x,y):
        cords = [-1,-1]
        if(55<=x<=95 and 55<y<95):
            cords=[0,0]
        elif(280<=x<=320 and 55<y<95):
            cords=[0,1]
        elif(505<=x<=545 and 55<y<95):
            cords=[0,2]
        elif(505<=x<=545 and 280<y<320):
            cords=[0,3]
        elif(505<=x<=545 and 505<y<545):
            cords=[0,4]
        elif(280<=x<=320 and 505<y<545):
            cords=[0,5]
        elif(55<=x<=95 and 505<y<545):
            cords=[0,6]
        elif(55<=x<=95 and 280<y<320):
            cords=[0,7]

        elif(130<=x<=170 and 130<y<170):
            cords=[1,0]
        elif(280<=x<=320 and 130<y<170):
            cords=[1,1]
        elif(430<=x<=470 and 130<y<170):
            cords=[1,2]
        elif(430<=x<=470 and 280<y<320):
            cords=[1,3]
        elif(430<=x<=470 and 430<y<470):
            cords=[1,4]
        elif(280<=x<=320 and 430<y<470):
            cords=[1,5]
        elif(130<=x<=170 and 430<y<470):
            cords=[1,6]
        elif(130<=x<=170 and 280<y<320):
            cords=[1,7]

        elif(205<=x<=245 and 205<y<245):
            cords=[2,0]
        elif(280<=x<=320 and 205<y<245):
            cords=[2,1]
        elif(355<=x<=395 and 205<y<245):
            cords=[2,2]
        elif(355<=x<=395 and 280<y<320):
            cords=[2,3]
        elif(335<=x<=395 and 335<y<395):
            cords=[2,4]
        elif(280<=x<=320 and 335<y<395):
            cords=[2,5]
        elif(205<=x<=245 and 335<y<395):
            cords=[2,6]
        elif(205<=x<=245 and 280<y<320):
            cords=[2,7]
        return cords

    def check_mill(self,pos1, pos2):
        mill = False
        compare = self.board[pos1][pos2]
        if(pos2%2==0):
            mill = (self.board[pos1][(pos2+1)%8]==compare and self.board[pos1][(pos2+2)%8]==compare) or (self.board[pos1][(pos2-1)%8]==compare and self.board[pos1][(pos2-2)%8]==compare)
        else:
            mill = (self.board[pos1][(pos2+1)%8]==compare and self.board[pos1][(pos2-1)%8]==compare) or (self.board[(pos1+1)%3][pos2]==compare and self.board[(pos1-1)%3][pos2]==compare)
        return mill

    def click(self, event):
        if(self.finish):
            self.game_over()
        elif(self.removal):
            self.remove_piece(event)
        elif(self.selected!=[-1,-1]):
            self.move(event)
        elif(self.phase==1):
            self.phase1(event)
        elif(self.phase==2):
            self.phase2(event)

    def remove_piece(self,event):
        other_player = 3-self.current_turn
        position = self.click_to_cord(event.x,event.y)
        can_remove = False
        if(self.board[position[0]][position[1]]==other_player):
            if(not self.check_mill(position[0],position[1])):
                can_remove = True
            else:
                can_remove = True
                for i in range(3):
                    for j in range(8):
                        if((i!=position[0] or j!=position[1]) and self.board[i][j]==other_player and not self.check_mill(i,j)):
                            can_remove = False
                            break
        if(can_remove):
            self.board[position[0]][position[1]] = 0
            self.removal = False
            if(self.current_turn==1):
                self.current_turn=2
            else:
                self.current_turn=1
            self.player_pieces[self.current_turn-1]-=1
            if(self.player_pieces[self.current_turn-1]<3 and self.phase==2):
                self.finish=True
        self.update_draw()

    def phase1(self,event):
        position = self.click_to_cord(event.x,event.y)
        if(position!= [-1,-1]):
            if(self.board[position[0]][position[1]]==0):
                self.board[position[0]][position[1]]=self.current_turn
                self.phase1_moves-=1
                self.player_pieces[self.current_turn-1]+=1
                if(self.check_mill(position[0],position[1])):
                    self.removal = True
                else:
                    if(self.current_turn==1):
                        self.current_turn=2
                    else:
                        self.current_turn=1
        self.update_draw()
        if(self.phase1_moves==0):
            self.phase = 2
            print('going to phase 2')

    def phase2(self,event):
        position = self.click_to_cord(event.x,event.y)
        if(position!=[-1,-1]):
            if(self.board[position[0]][position[1]]==self.current_turn):
                self.selected = position

    def next_to(self, pos1, pos2):
        neighbours = False
        if(pos1[0]==pos2[0] and (abs(pos1[1]-pos2[1])==1 or abs(pos1[1]-pos2[1])==7)):
            neighbours = True
        if(pos1[1]==pos2[1] and abs(pos1[0]-pos2[0])==1):
            neighbours = pos1[1]%2==1
        return neighbours

    def move(self,event):
        position = self.click_to_cord(event.x,event.y)
        if(position!= [-1,-1]):
            if(self.board[position[0]][position[1]]==0):
                if(self.player_pieces[self.current_turn-1]>3):
                    print(position)
                    print(self.selected)
                    if(self.next_to(position,self.selected)):
                        self.board[position[0]][position[1]]=self.current_turn
                        self.board[self.selected[0]][self.selected[1]] = 0
                        self.selected = [-1,-1]
                        if(self.check_mill(position[0],position[1])):
                            self.removal = True
                        else:
                            if(self.current_turn==1):
                                self.current_turn=2
                            else:
                                self.current_turn=1
                        self.update_draw()
                    else:
                        self.selected = [-1,-1]
                        self.update_draw()
                else:
                    self.board[position[0]][position[1]]=self.current_turn
                    self.board[self.selected[0]][self.selected[1]] = 0
                    self.selected = [-1,-1]
                    if(self.check_mill(position[0],position[1])):
                        self.removal = True
                    else:
                        if(self.current_turn==1):
                            self.current_turn=2
                        else:
                            self.current_turn=1
                    self.update_draw()
            else:
                self.selected = [-1,-1]
                self.update_draw()

    def game_over(self):
        self.canvas.delete('all')
        if(self.player_pieces[0]<3):
            self.canvas.create_text(300, 300, font="cmr 25 bold", fill='black', text='player 2 wins!')
        else:
            self.canvas.create_text(300, 300, font="cmr 25 bold", fill='black', text='player 1 wins!')


game_instance = NMM_board()
game_instance.mainloop()
