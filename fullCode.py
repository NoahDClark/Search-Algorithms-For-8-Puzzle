class node:
    
    def __init__(self,parent,tiles,depth,heuristic):
        self._parent = parent
        self._tiles = tiles
        self._depth = depth
        
        if(heuristic == 0):
            self._heuristic = 0
        else:
            self._heuristic = evalHN(tiles)
        
        self._fn = self._depth + self._heuristic
        
        
    def getTiles(self):
        #print(self._tiles)
        return self._tiles
    
#    def __eq__(self, other):
 #       return (self._fn == other._fn) and (self._depth == other._depth)
    
    def __lt__(self, other):
        return (self._fn < other._fn)

    def __gt__(self, other):
        return (self._fn > other._fn)

def appendMoves(nodeQueue):
    pqInstance = False
    if isinstance(nodeQueue, PriorityQueue):
        pqInstance = True
        current = nodeQueue.queue[0][1]
        nodeQueue.get(0)
    else:
        current = nodeQueue[0]
        nodeQueue.pop(0)
    
    x, y = 0,0
    for i in range(3):
        for j in range(3):
            if (current._tiles[i][j] == 0):
                x = i
                y = j
    #print("BEFORE")
    if (x<2):
        #print(current.getTiles())
        temp1 = moveUP(current,x,y)
        if pqInstance:
            nodeQueue.put((temp1._fn, temp1))
        else:
            nodeQueue.append(temp1)
        
    if (y<2):
        #print(current.getTiles())
        temp2 = moveRIGHT(current,x,y)
        if pqInstance:
            nodeQueue.put((temp2._fn, temp2))
        else:
            nodeQueue.append(temp2)
        
    if (x>0):
        #print(current.getTiles())
        temp3 = moveDOWN(current,x,y)
        if pqInstance:
            nodeQueue.put((temp3._fn, temp3))
        else:
            nodeQueue.append(temp3)
        
    if (y>0):
        temp = moveLEFT(current,x,y)
        if pqInstance:
            nodeQueue.put((temp._fn, temp))
        else:
            nodeQueue.append(temp)
            
    #for i in range(len(nodeQueue.queue)):
    #    print (nodeQueue.queue[i][1]._tiles)
    #print("AFTER")
    
def moveUP(currentNode,x,y):
    tempDepth = -1
    if(currentNode._depth != -1):
        tempDepth = currentNode._depth + 2
    tempTiles = [row[:] for row in currentNode.getTiles()]
    tempVal = tempTiles[x+1][y]
    tempTiles[x+1][y] = 0
    tempTiles[x][y] = tempVal
    if (currentNode._heuristic == 0):
        outputNode = node(currentNode,tempTiles,tempDepth,0)
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles))
    return outputNode

def moveRIGHT(currentNode,x,y):
    tempDepth = -1
    if(currentNode._depth != -1):
        tempDepth = currentNode._depth + 2
    tempTiles = [row[:] for row in currentNode.getTiles()]
    tempVal = tempTiles[x][y+1]
    tempTiles[x][y+1] = 0
    tempTiles[x][y] = tempVal
    if (currentNode._heuristic == 0):
        outputNode = node(currentNode,tempTiles,tempDepth,0)
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles))
    return outputNode
        
def moveDOWN(currentNode,x,y):
    tempDepth = -1
    if(currentNode._depth != -1):
        tempDepth = currentNode._depth + 2
    tempTiles = [row[:] for row in currentNode.getTiles()]
    tempVal = tempTiles[x-1][y]
    tempTiles[x-1][y] = 0
    tempTiles[x][y] = tempVal
    if (currentNode._heuristic == 0):
        outputNode = node(currentNode,tempTiles,tempDepth,0)
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles))
    return outputNode

def moveLEFT(currentNode,x,y):
    tempDepth = -1
    if(currentNode._depth != -1):
        tempDepth = currentNode._depth + 2
    tempTiles = [row[:] for row in currentNode.getTiles()]
    tempVal = tempTiles[x][y-1]
    tempTiles[x][y-1] = 0
    tempTiles[x][y] = tempVal
    if (currentNode._heuristic == 0):
        outputNode = node(currentNode,tempTiles,tempDepth,0)
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles))
    return outputNode


def notFinalState(currentNode):
    tempTiles = currentNode.getTiles()
    final = [[0 for i in range(3)] for j in range(3)]
    final[0][0] = 1
    final[0][1] = 2
    final[0][2] = 3
    final[1][0] = 8
    final[1][1] = 0
    final[1][2] = 4
    final[2][0] = 7
    final[2][1] = 6
    final[2][2] = 5
    
    if(tempTiles != final):
        return True
    else:
        return False
    
def evalHN(currentTiles):
    hn = 0
    tempTiles = [row[:] for row in currentTiles]
    
    if (tempTiles[2][1] != 0):
        hn = hn + 1
    if ((tempTiles[0][0] != tempTiles[0][1]-1) or (tempTiles[0][0] == tempTiles[0][1]+7)):
        #print("trigger 1")
        hn = hn+2
    if ((tempTiles[0][1] != tempTiles[0][2]-1) or (tempTiles[0][1] == tempTiles[0][2]+7)):
        #print("trigger 2")
        hn = hn+2
    if ((tempTiles[0][2] != tempTiles[1][2]-1) or (tempTiles[0][2] == tempTiles[1][2]+7)):
        #print("trigger 3")
        hn = hn+2
    if ((tempTiles[1][2] != tempTiles[2][2]-1) or (tempTiles[1][2] == tempTiles[2][2]+7)):
        #print("trigger 4")
        hn = hn+2
    if ((tempTiles[2][2] != tempTiles[2][1]-1) or (tempTiles[2][2] == tempTiles[2][1]+7)):
        #print("trigger 5")
        hn = hn+2
    if ((tempTiles[2][1] != tempTiles[2][0]-1) or (tempTiles[2][1] == tempTiles[2][0]+7)):
        #print("trigger 6")
        hn = hn+2
    if ((tempTiles[2][0] != tempTiles[1][0]-1) or (tempTiles[2][0] == tempTiles[1][0]+7)):
        #print("trigger 7")
        hn = hn+2
    if ((tempTiles[1][0] != tempTiles[0][0]-1) or (tempTiles[1][0] == tempTiles[0][0]+7)):
        #print("trigger 8")
        hn = hn+2
        
    hn = hn*3
    return hn


from queue import PriorityQueue
import time

def UCSMethod(firstNode):
    
    start_time = time.time()
    nodeQueue = PriorityQueue()
    nodeQueue.put((firstNode._fn, firstNode))
    count = 0
    
    while(notFinalState(nodeQueue.queue[0][1])):
        count = count+1
        appendMoves(nodeQueue)
        if(count > 100000):
            break

    #print(count)
    tt = (time.time() - start_time)
    return nodeQueue.queue[0][1]._tiles, count, tt

def BFSMethod(firstNode):
    
    start_time = time.time()
    nodeQueue = PriorityQueue()
    nodeQueue.put((firstNode._fn, firstNode))
    count = 0
    
    while(notFinalState(nodeQueue.queue[0][1])):
        count = count+1
        appendMoves(nodeQueue)
        if(count > 100000):
            break

    tt = (time.time() - start_time)
    return nodeQueue.queue[0][1]._tiles, count, tt

def AStarMethod(firstNode):
    
    start_time = time.time()
    nodeQueue = PriorityQueue()
    nodeQueue.put((firstNode._fn, firstNode))
    count = 0
    previous = None
    
    while(notFinalState(nodeQueue.queue[0][1])):
        count = count+1
        appendMoves(nodeQueue)
        if(count > 100000):
            break

    tt = (time.time() - start_time)
    return nodeQueue.queue[0][1]._tiles, count, tt
    
def DFSMethod(firstNode):
    
    start_time = time.time()
    nodeQueue = []
    nodeQueue.append(firstNode)
    count = 0
    previous = None
    
    while(notFinalState(nodeQueue[0])):
        count = count+1
        appendMoves(nodeQueue)
        if(count > 100000):
            break
        
    tt = (time.time() - start_time)
    return nodeQueue[0]._tiles, count, tt
    
    
import random
def randomBoard():
    tempArray = [0, 1,2,3,4,5,6,7,8]
    outArray = [[0 for i in range(3)] for j in range(3)]
    
    for i in range(3):
        for j in range(3):
            temp = random.randint(0,100)%len(tempArray)
            outArray[i][j] = tempArray[temp]
            tempArray.pop(temp)
            
    return outArray


arrayOne = [[0 for i in range(3)] for j in range(3)]
arrayOne[0][0] = 2
arrayOne[0][1] = 8
arrayOne[0][2] = 3
arrayOne[1][0] = 1
arrayOne[1][1] = 6
arrayOne[1][2] = 4
arrayOne[2][0] = 7
arrayOne[2][1] = 0
arrayOne[2][2] = 5
#196, 7, 7, 215
arrayTwo = [[0 for i in range(3)] for j in range(3)]
arrayTwo[0][0] = 2
arrayTwo[0][1] = 0
arrayTwo[0][2] = 3
arrayTwo[1][0] = 1
arrayTwo[1][1] = 8
arrayTwo[1][2] = 4
arrayTwo[2][0] = 7
arrayTwo[2][1] = 6
arrayTwo[2][2] = 5
#19, 5, 5, 31
arrayThree = [[0 for i in range(3)] for j in range(3)]
arrayThree[0][0] = 1
arrayThree[0][1] = 2
arrayThree[0][2] = 3
arrayThree[1][0] = 7
arrayThree[1][1] = 8
arrayThree[1][2] = 0
arrayThree[2][0] = 6
arrayThree[2][1] = 5
arrayThree[2][2] = 4
#231, 7, 13, 146
arrayFour = [[0 for i in range(3)] for j in range(3)]
arrayFour[0][0] = 1
arrayFour[0][1] = 8
arrayFour[0][2] = 2
arrayFour[1][0] = 7
arrayFour[1][1] = 0
arrayFour[1][2] = 3
arrayFour[2][0] = 6
arrayFour[2][1] = 5
arrayFour[2][2] = 4
#3555, 655, 171, 7103

presetList = []
presetList.append(arrayOne)
presetList.append(arrayTwo)
presetList.append(arrayThree)
presetList.append(arrayFour)











#Import tkinter library
from tkinter import *
from matplotlib import pyplot as plt
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
#fig = plt.figure()
#plt.figure().clear()
#plt.close()
#plt.cla()
#plt.clf()
#Create an instance of Tkinter frame or window
window = Tk()
fig = Figure(figsize = (5, 5),dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = window)  

labelOne = Label(window, text="Current Starting Board:    ", font=("Times",36)).place(x=300,y=200)
labelTwo = Label(window, text="Nodes visited when solving with DFS: ", font=("Times",14)).place(x=850,y=150)
labelThree = Label(window, text="Nodes visited when solving with UCS: ", font=("Times",14)).place(x=850,y=300)
labelFour = Label(window, text="Nodes visited when solving with BFS: ", font=("Times",14)).place(x=850,y=450)
labelFive = Label(window, text="Nodes visited when solving with A*: ", font=("Times",14)).place(x=850,y=600)
#labelFour = Label(window, text="TEMP LINE \n TEMP LINE \n TEMP LINE \n TEMP LINE.\n TEMP LINE \n TEMP LINE.", font=("Times",14)).place(x=850,y=600)

canvas.draw()
canvas.get_tk_widget().place(x=300,y=200)
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

class containsValues():
    def __init__(self, currentVal, arrayList, array):
        self.currentVal = currentVal
        self.aList = arrayList
        self.currentTiles = array
    def getArray(self, val):
        return self.aList[val]

tempVals = containsValues(0,presetList, arrayOne)

    
#Set the geometry of tkinter frame
window.geometry("1200x800")



def plotGame():
    tiles = randomBoard()
    tempVals.currentTiles = tiles
    string = "Current Starting Board:    \n "
    string = string + "---------------------- \n"
    for i in range(3):
        for j in range(3):
            string = string + "  |  "
            string = string + str(tiles[i][j])
            if j == 2:
                string = string + "  |  "
        string = string + "\n ---------------------- \n"
    
    labelOne = Label(window, text=string, font=("Times",36)).place(x=300,y=200)
    stringTwo = "Nodes visited, time when solving with DFS: \n\n"
    labelTwo = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=150)
    stringTwo = "Nodes visited, time when solving with UCS: \n\n"
    labelThree = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=300)
    stringTwo = "Nodes visited, time when solving with BFS: \n\n"
    labelFour = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=450)
    stringTwo = "Nodes visited, time when solving with A*: \n\n"
    labelFive = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=600)

def plotNonRandomGame():
    tempCV = tempVals.currentVal%4
    print(tempCV)
    tiles = tempVals.getArray(tempCV)
    tempVals.currentTiles = tiles
    tempVals.currentVal = tempVals.currentVal + 1
    string = "Current Starting Board:    \n "
    string = string + "---------------------- \n"
    for i in range(3):
        for j in range(3):
            string = string + "  |  "
            string = string + str(tiles[i][j])
            if j == 2:
                string = string + "  |  "
        string = string + "\n ---------------------- \n"
    
    labelOne = Label(window, text=string, font=("Times",36)).place(x=300,y=200)
    stringTwo = "Nodes visited, time when solving with DFS: \n\n"
    labelTwo = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=150)
    stringTwo = "Nodes visited, time when solving with UCS: \n\n"
    labelThree = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=300)
    stringTwo = "Nodes visited, time when solving with BFS: \n\n"
    labelFour = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=450)
    stringTwo = "Nodes visited, time when solving with A*: \n\n"
    labelFive = Label(window, text=stringTwo, font=("Times",14)).place(x=850,y=600)
    

def solveWithDFS():
    DFSNode = node(None, tempVals.currentTiles, 0, -1)
    
    string = "Nodes visited, time when solving with DFS: \n\n"
    unused, nodesVisited, ttt = DFSMethod(DFSNode)
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelTwo = Label(window, text=string, font=("Times",14)).place(x=850,y=150)
    
    
def solveWithUCS():
    UCSNode = node(None, tempVals.currentTiles, 0, 0)
    
    string = "Nodes visited, time when solving with UCS: \n\n"
    unused, nodesVisited, ttt = UCSMethod(UCSNode)
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelThree = Label(window, text=string, font=("Times",14)).place(x=850,y=300)

def solveWithBFS():
    BFSNode = node(None, tempVals.currentTiles, -1, evalHN(tempVals.currentTiles))
    
    string = "Nodes visited, time when solving with BFS: \n\n"
    unused, nodesVisited, ttt = BFSMethod(BFSNode)
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelFour = Label(window, text=string, font=("Times",14)).place(x=850,y=450)
    
def solveWithAStar():
    aStarNode = node(None, tempVals.currentTiles, 0, evalHN(tempVals.currentTiles))
    unused, nodesVisited, ttt = AStarMethod(aStarNode)
    string = "Nodes visited, time when solving with A*: \n\n"
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelFive = Label(window, text=string, font=("Times",14)).place(x=850,y=600)
    
    
    
buttonOne=Button(window, height = 4, width = 20, text="Display Random Game", command = plotGame)
buttonOne.pack(ipadx=10)
buttonOne.place(x=50,y=150)

buttonTwo=Button(window, height = 4, width = 20, text="Solve With DFS", command= solveWithDFS)
buttonTwo.pack(ipadx=10)
buttonTwo.place(x=50,y=250)

buttonThree=Button(window, height = 4, width = 20, text="Solve With UCS", command= solveWithUCS)
buttonThree.pack(ipadx=10)
buttonThree.place(x=50,y=350)

buttonFour=Button(window, height = 4, width = 20, text="Solve With BFS", command= solveWithBFS)
buttonFour.pack(ipadx=10)
buttonFour.place(x=50,y=450)

buttonFive=Button(window, height = 4, width = 20, text="Solve With A*", command= solveWithAStar)
buttonFive.pack(ipadx=10)
buttonFive.place(x=50,y=550)


buttonSix=Button(window, height = 4, width = 20, text="Display Non-Random Game", command= plotNonRandomGame)
buttonSix.pack(ipadx=10)
buttonSix.place(x=50,y=50)

plotGame()
# place the button 
# in main window

window.bind('<Return>',lambda event:callback())
window.mainloop()
presetList.append(arrayFour)
