import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


plt.subplots_adjust(bottom=0.15)


color=1
chessboard=np.zeros((10,10))
chessboard[1::2,0::2]=color
chessboard[0::2,1::2]=color
player1=[(0,1),(0,3),(0,5),(0,7),(0,9),
		(1,0),(1,2),(1,4),(1,6),(1,8),
		(2,1),(2,3),(2,5),(2,7),(2,9),
		(3,0),(3,2),(3,4),(3,6),(3,8)]
player2=[(6,1),(6,3),(6,5),(6,7),(6,9),
		(7,0),(7,2),(7,4),(7,6),(7,8),
		(8,1),(8,3),(8,5),(8,7),(8,9),
		(9,0),(9,2),(9,4),(9,6),(9,8)]
x1,y1 = zip(*player1)
x2,y2 = zip(*player2)
 #plt.axis('off')
plt.tick_params(
bottom=False,      # ticks along the bottom edge are off
top=False,         # ticks along the top edge are off
left=False,
labelleft=False,
labelbottom=False) # labels along the bottom edge are off

plt.scatter(y1,x1, s=200, c='red', marker='o')
plt.scatter(y2,x2, s=200, c='brown', marker='o')
plt.imshow(chessboard, cmap='Blues')
   


class Index(object):
    ind = 0

    def next(self, event):
        sys.exit(main(sys.argv))

    def prev(self, event):
        sys.exit(main(sys.argv))

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
