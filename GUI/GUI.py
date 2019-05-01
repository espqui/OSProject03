
from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
def pickMovement():
	if currentPlayer.get()==1:
		lastMovementVariable.set('Last Movement: Player %d picked %s Position' % (currentPlayer.get(), player1[numberChosen.current()]))

		
	else:
		lastMovementVariable.set('Last Movement: Player %d picked %s Position' % (currentPlayer.get(), player2[numberChosen.current()]))

	
def dropMovement():
	
	if currentPlayer.get()==1:
		lastMovementVariable.set('Last Movement: Player %d Dropped on %s Position' % (currentPlayer.get(), player1[numberChosen.current()]))
		currentPlayer.set(2)
		numberChosen['values'] = player2
		
		
	else:
		lastMovementVariable.set('Last Movement: Player %d Dropped on %s Position' % (currentPlayer.get(), player2[numberChosen.current()]))
		currentPlayer.set(1)
		numberChosen['values'] = player1

def InitCurrentPlayer(currentPlayer):
	label=ttk.Label(root, text="CurrentPlayer")
	label.pack()
	Label(root, textvariable=currentPlayer).pack() 
	currentPlayer.set(1)
def lastMovement(lastMovementVariable):
	Label(root, textvariable=lastMovementVariable).pack()
	lastMovementVariable.set("Last Movement")  


def initBoardParameters(player1,player2,numberChosen,currentPlayer):
	color=1
	chessboard=np.zeros((10,10))
	chessboard[1::2,0::2]=color
	chessboard[0::2,1::2]=color
	x1,y1 = zip(*player1)
	x2,y2 = zip(*player2)
	figure3 = plt.Figure(figsize=(5,4), dpi=100)
	ax3 = figure3.add_subplot(111)
	ax3.imshow(chessboard, cmap='Blues')
	ax3.scatter(y1,x1, s=200, c='red', marker='o')
	ax3.scatter(y2,x2, s=200, c='brown', marker='o')
	scatter3 = FigureCanvasTkAgg(figure3, root) 
	scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)	
	
	label=ttk.Label(root, text="Position")
	label.pack()
	
	numberChosen['values'] = player1
	numberChosen.pack()
	
	b = Button(root,compound=TOP, text="Pick", command=pickMovement)
	b.pack()
	b = Button(root,compound=TOP, text="Drop", command=dropMovement)
	
	b.pack()


	

def search(player,posXBefore,posYBefore,posXAfter,posYAfter):
	index_list = [x for x, y in enumerate(player) if y[0] == posXBefore and y[1] == posYBefore ]
	player[index_list[0]]=(posXAfter,posYAfter)
	return (player)
				

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    root= tk.Tk()
    currentPlayer=IntVar()
    numberChosen = ttk.Combobox(root, width=12)
    lastMovementVariable = StringVar()
    player2=[(6,1),(6,3),(6,5),(6,7),(6,9),
			(7,0),(7,2),(7,4),(7,6),(7,8),
			(8,1),(8,3),(8,5),(8,7),(8,9),
			(9,0),(9,2),(9,4),(9,6),(9,8)] 
    player1=[(0,1),(0,3),(0,5),(0,7),(0,9),
			(1,0),(1,2),(1,4),(1,6),(1,8),
			(2,1),(2,3),(2,5),(2,7),(2,9),
			(3,0),(3,2),(3,4),(3,6),(3,8)]
	
    initBoardParameters(player1, player2,numberChosen, currentPlayer)
    InitCurrentPlayer(currentPlayer)
    lastMovement(lastMovementVariable)
    root.mainloop()
    sys.exit(main(sys.argv))
   




