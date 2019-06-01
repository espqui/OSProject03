import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import IntVar
from functools import partial
import numpy as np
import time

from ctypes import *
import os 
root_path = os.path.dirname(os.path.realpath(__file__))

libFinger = CDLL(root_path + "/../library/libfinger.so")

 
#call C function to check connection
libFinger.connect() 
libFinger.set_device()

#####################################################
#All player's movements are developed in this function
###################################################
def playerAction(i,j,event):
	global pick,pickPos,currentPlayer, board
	#print("pick value",pick)
	pickAux=pick
	if(pick==1 and (board[i,j]==1 or board[i,j]==2)):
		if(board[i,j]==1):
			currentPlayer=1
		elif(board[i,j]==2):
			currentPlayer=2
		pickPos=(i,j)
		pick=0
		board[i,j]=3
		#print("picked",pickPos)
		update()
	elif(pick==0 and board[i,j]==3):
		#################################
		#drop chip on i,j position
		#libDriver.methodDrop(i,j)
		#varRand = libDriver.randNum()
		#print("Random Number:", varRand)
	    ################################

		dropPos=(i,j)
	
		pick=1
		if(currentPlayer==1):
			board[i,j]=1
			
		elif(currentPlayer==2):
			board[i,j]=2	
		update()

#####################################################
#Refresh the board when the movement has finished
###################################################
def update():
	global board
	for i in range(0,10):
		for j in range(0,10):
			if board[i,j]==1:
				buttonPlayer[i*5+j//2].config(image=chip1)
			elif board[i,j]==2:
				buttonPlayer[i*5+j//2].config(image=chip2)
			elif board[i,j]==3:
				buttonPlayer[i*5+j//2].config(image=chip3)
			
#####################################################
#Look for all empthy spaces  or those with a chip, 
#the result is shown in the comboBox element.
#####################################################
def search(free):
	global numberChosen,board
	answer=[]
	for i in range(0,10):
		for j in range(0,10):
			if (board[i,j]==1 or board[i,j]==2) and free==False:
				answer.append((i,j))
			elif (board[i,j]==3 and free==True):
				answer.append((i,j))
	numberChosen['values'] = answer
				
#####################################################
# This function is called when a player remove a chip 
# of his opponent and the score is updated
#####################################################
def removeChip(i,j,event):
	global board
	#################################
	#remove chip i,j position
	################################
	
	#libFinger.move(i+1,j+1)	
	#libFinger.pick()
	
	
	
	buttonPlayer[i*5+j//2].config(image=chip3)
	if(board[i,j]==1):
		print(pointP2.get()+1)
		pointP2.set(pointP2.get()+1)
	elif(board[i,j]==2):
		print(pointP1.get()+1)
		pointP1.set(pointP1.get()+1)
	board[i,j]=3

#####################################################
# Used when the player press the button pick
#####################################################
def pickMovement():
	global pick,dropButton,pickButton
	pick=1
	dropButton.config(bg="#d9d9d9")
	pickButton.config(bg="green")
	print("picked")
	search(False)
#####################################################
# Used when the player press the button drop
#####################################################
def dropMovement():
	search(True)
	global pick,dropButton,pickButton
	pick=0
	dropButton.config(bg="green")
	pickButton.config(bg="#d9d9d9")
	print("dropped")
	search(True)
#####################################################
# Used when the player press the button Move
#####################################################	
def move():
	global dropButton,pickButton
	dropButton.config(bg="#d9d9d9")
	pickButton.config(bg="#d9d9d9")
	playerAction(int(numberChosen.get()[0]),int(numberChosen.get()[2]),0)

	
root = tk.Tk()
board=np.zeros([10,10],dtype = int) 


#initBoard
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)
chip1 = tk.PhotoImage(file="./pictures/chip1.png")#chip of player 1
chip2 = tk.PhotoImage(file="./pictures/chip2.png")#chip of player 2
chip3 = tk.PhotoImage(file="./pictures/free.png")#empty space

buttonPlayer = list() # Each position on the board is a button
pick=1#0drop, 1, pick, -1 invalid field was selected
pickPos=(0,0)
currentPlayer=True
pointP1 = IntVar()
pointP2 = IntVar()
pointP1.set(0)
pointP2.set(0)
tk.Label(frame1, text=' Points:', width=10).grid(row=5,column=10)
tk.Label(frame1, text=' Player1:', width=10).grid(row=6,column=10)
tk.Label(frame1, textvariable =pointP1, width=5).grid(row=6,column=11)
tk.Label(frame1, text=' Player2', width=10).grid(row=7,column=10)
tk.Label(frame1, textvariable =pointP2, width=5).grid(row=7,column=11)
numberChosen = tk.ttk.Combobox(frame1, width=12)

#Create the board#
for i in range(0,10):
	for j in range(0,10):
		if i%2==0:
			if j%2 ==1:
				buttonPlayer.append(tk.Button(frame1, image=chip3))
				buttonPlayer[-1].bind('<Button-1>', partial(playerAction, i,j))
				buttonPlayer[-1].bind('<Button-3>', partial(removeChip, i,j))
				buttonPlayer[-1].grid(row=i,column=j)
				if i<=4:
					board[i][j]=1
				elif i>4 and i <7:
					board[i][j]=3
				else:
					board[i][j]=2
		else:
			if j%2 ==0:
				buttonPlayer.append(tk.Button(frame1, image=chip3))
				buttonPlayer[-1].bind('<Button-1>', partial(playerAction, i,j))
				buttonPlayer[-1].bind('<Button-3>', partial(removeChip, i,j))
				buttonPlayer[-1].grid(row=i,column=j)
				if i<=4:
					board[i][j]=1
				elif i>4 and i <7:
					board[i][j]=3	
				else:
					board[i][j]=2
update()			
#Show empty spaces
for i in range(0,10,2):
	for j in range(0,10,2):
		tk.Label(frame1, bg="white",width="7", height="4").grid(row=i, column=j)
for i in range(1,10,2):
	for j in range(1,10,2):
		tk.Label(frame1, bg="white",width="7", height="4").grid(row=i, column=j)


########## MENU on the right side #####################	
label=tk.Label(frame1, text="Position")
label.grid(row=0, column=10)

numberChosen.grid(row=1, column=10)
#########################################################
#Buttons: pick, drop and move
#########################################################3
pickButton = tk.Button(frame1,compound=TOP, text="Pick", command=pickMovement)
pickButton.grid(row=0, column=11)
dropButton = tk.Button(frame1,compound=TOP, text="Drop", command=dropMovement)
dropButton.grid(row=0, column=12)
pickButton.config(bg="#d9d9d9")	
moveButton = tk.Button(frame1,compound=TOP, text="Move", command=move)
moveButton.grid(row=1, column=12)	

root.mainloop()
	
		
