#This program uses A Star (A*), Best First Search (BFS), Uniform Cost Search(UCS), and Depth First Search (DFS)
#Note that BFS is NOT BREADTH FIRST SEARCH. It is BEST first search, meaning it uses a heuristic. 


#This is the node class, used in all four algorithms. 
#It contains a parent node, tiles, depth, heuristic value, and information on how the tile previously moved.
class node:
    
    #There are a few quirks about this constructor to allow the program to function with all four algorithms.
    #Most importantly, if heuristic == 0 it will not run evalHN and just keep it set to 0.
    def __init__(self,parent,tiles,depth,heuristic, moved):
        self._parent = parent
        self._tiles = tiles
        self._depth = depth
        self._moved = moved
        
        if(heuristic == 0):
            self._heuristic = 0
        else:
            self._heuristic = evalHN(tiles)
        
        self._fn = self._depth + self._heuristic
        
    #I mostly use node._tiles throughout the program, but on occasion I will call this function to get tiles.
    def getTiles(self):
        return self._tiles
    
    #Comparison functions, set to compare the node using f(n) value.
    #This one is not used currently
    #def __eq__(self, other):
        #return (self._fn == other._fn) and (self._depth == other._depth)
    
    def __lt__(self, other):
        return (self._fn < other._fn)

    def __gt__(self, other):
        return (self._fn > other._fn)

    

#Append move is one of the most important functions in the program. 
#Firstly, it checks to see if it is a priorityQueue instance. Note that this is only false IF DFS is calling the function
#Next, it will then find the location of the zero value and then call the appropriate movement function.
def appendMoves(nodeQueue, stackVisited=None):
    #Checks if DFS is used or not
    pqInstance = False
    if isinstance(nodeQueue, PriorityQueue):
        pqInstance = True
        current = nodeQueue.queue[0][1]
        nodeQueue.get(0)
    else:
        current = nodeQueue[len(nodeQueue)-1]
        stackVisited.append(current._tiles)
        nodeQueue.pop()
    
    #Finds location of empty space on puzzle(zero)
    x, y = 0,0
    for i in range(3):
        for j in range(3):
            if (current._tiles[i][j] == 0):
                x = i
                y = j
    
    #Calls the appropriate movement option, either up, down, left, or right.
    if (x<2):
        temp1 = moveUP(current,x,y)
        if pqInstance:
            nodeQueue.put((temp1._fn, temp1))
        else:
            nodeQueue.append(temp1)
        
    if (y<2):
        temp2 = moveRIGHT(current,x,y)
        if pqInstance:#NDC
            nodeQueue.put((temp2._fn, temp2))
        else:
            nodeQueue.append(temp2)
        
    if (x>0):
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
            

#This method, along with the next three, will swap the empty space (zero) with another number.
#As suggested by the name, it either moves the tile up, down, left, or right.
#How each of them work: if depth is NOT -1, add one depth (which is done by adding two since var starts at -1)
#Then, copy array and swap tiles by either adding/subtracting to x or y. Then return a new node.
#Why is there a tempDepth = -1? Because, this allows the program to ignore depth if BFS or DFS is being called.
def moveUP(currentNode,x,y):
    tempDepth = -1
    if(currentNode._depth != -1):
        tempDepth = currentNode._depth + 2
    tempTiles = [row[:] for row in currentNode.getTiles()]
    tempVal = tempTiles[x+1][y]
    tempTiles[x+1][y] = 0
    tempTiles[x][y] = tempVal
    if (currentNode._heuristic == 0):
        outputNode = node(currentNode,tempTiles,tempDepth,0, "Move Down") #Why is "Move Down" here? Because this function is actually moveDown, oops. This was the easiest bug fix, sorry.
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles), "Move Down")  #This does not change how the algorithm works
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
        outputNode = node(currentNode,tempTiles,tempDepth,0, "Move Right")
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles), "Move Right")
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
        outputNode = node(currentNode,tempTiles,tempDepth,0, "Move Up") #This does not change how the algorithm works
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles), "Move Up") #Why is "Move Up" here? Because this function is actually moveUP, oops. This was the easiest bug 
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
        outputNode = node(currentNode,tempTiles,tempDepth,0, "Move Left")
    else:
        outputNode = node(currentNode,tempTiles,tempDepth,evalHN(tempTiles), "Move Left")
    return outputNode



#Method used to check if the node has reached the goal state. It simply compares goal array to current array.
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
    #print(final)
    
    if(tempTiles != final):
        return True
    else:
        return False
    
    
#Heuristic function!
#This function uses a form of nilsson heuristic. So h(n) = P(n) + 3*S(n)
def evalHN(currentTiles):
    hn = 0
    tempTiles = [row[:] for row in currentTiles]
    
    if (tempTiles[2][1] != 0):
        hn = hn + 1
    if ((tempTiles[0][0] != tempTiles[0][1]-1) or (tempTiles[0][0] == tempTiles[0][1]+7)):
        hn = hn+2
        
    if ((tempTiles[0][1] != tempTiles[0][2]-1) or (tempTiles[0][1] == tempTiles[0][2]+7)):
        hn = hn+2
        
    if ((tempTiles[0][2] != tempTiles[1][2]-1) or (tempTiles[0][2] == tempTiles[1][2]+7)):
        hn = hn+2
        
    if ((tempTiles[1][2] != tempTiles[2][2]-1) or (tempTiles[1][2] == tempTiles[2][2]+7)):
        hn = hn+2
        
    if ((tempTiles[2][2] != tempTiles[2][1]-1) or (tempTiles[2][2] == tempTiles[2][1]+7)):
        hn = hn+2
        
    if ((tempTiles[2][1] != tempTiles[2][0]-1) or (tempTiles[2][1] == tempTiles[2][0]+7)):
        hn = hn+2
        
    if ((tempTiles[2][0] != tempTiles[1][0]-1) or (tempTiles[2][0] == tempTiles[1][0]+7)):
        hn = hn+2
        
    if ((tempTiles[1][0] != tempTiles[0][0]-1) or (tempTiles[1][0] == tempTiles[0][0]+7)):
        hn = hn+2
        
    hn = hn*3
    return hn #returns heuristic value


from queue import PriorityQueue
import time

#Now for UCS, DFS, BFS, and A*
#Note that there is not much code contained within these functions. 
#In fact, UCS, BFS, and AStar are the exact same! Let me explain why and how this works:
#Why: I could replace all of these methods with just one but I separted them for clarity when calling them below.
#How this works: As noted above, heuristic will always be zero if node starts at zero.
#That allows the previous functions to act as if there is no heuristic.
#Similarly if depth starts at -1, the previous functions will keep it at -1, effectively ignoring depth.
#Starting values: h(n) = 0 and g(n) = 0 is UCS
#Starting values: h(n) > 0 and g(n) = -1 is BFS
#Starting values: h(n) > 0 and g(n) = 0 is UCS
#Anything else is DFS

def UCSMethod(firstNode): #Takes in a node
    
    start_time = time.time() #Used to track time
    nodeQueue = PriorityQueue() #Priority queue
    nodeQueue.put((firstNode._fn, firstNode))
    count = 0
    
    while(notFinalState(nodeQueue.queue[0][1])): #Continues until final state is found
        count = count+1
        appendMoves(nodeQueue) #Calls appendMoves, most imporant function here
        if(count > 200000): #Break at 100000 nodes to stop program from running endlessly and killing my computer
            break

    tt = (time.time() - start_time)
    return nodeQueue.queue[0][1], count, tt #return node, node count, and time

def BFSMethod(firstNode):
    
    start_time = time.time()
    nodeQueue = PriorityQueue()
    nodeQueue.put((firstNode._fn, firstNode))
    count = 0
    
    while(notFinalState(nodeQueue.queue[0][1])):
        count = count+1
        appendMoves(nodeQueue)
        if(count > 200000):
            break

    tt = (time.time() - start_time)
    return nodeQueue.queue[0][1], count, tt

def AStarMethod(firstNode):
    
    start_time = time.time()
    nodeQueue = PriorityQueue()
    nodeQueue.put((firstNode._fn, firstNode))
    count = 0
    
    while(notFinalState(nodeQueue.queue[0][1])):
        count = count+1
        appendMoves(nodeQueue)
        if(count > 200000):
            break

    tt = (time.time() - start_time)
    return nodeQueue.queue[0][1], count, tt
    
#Different from the previous three since it uses a stack.
def DFSMethod(firstNode): #Takes in a node
    
    start_time = time.time()
    nodeStack = [] 
    nodeStack.append(firstNode) #Appends first node to stack
    visitedNodes = [] #array of visited nodes to stop DFS from getting stuck in a loop of left right left right...
    count = 0
    previous = None
    
    while(notFinalState(nodeStack[len(nodeStack)-1])): #While most recent node (last one) is not final state:
        count = count+1 #NDC
        if nodeStack[len(nodeStack)-1]._tiles not in visitedNodes: #Makes sure node has not already been checked
            appendMoves(nodeStack, visitedNodes) #Calls appendMoves, most important function
        else:
            nodeStack.pop() #pops off nodes that have already been visited
            count = count - 1
        if(count > 25000): #Stops loop from destroying my computer by capping nodes at 100000
            break
        
    tt = (time.time() - start_time)
    return nodeStack[len(nodeStack)-1], count, tt #returns last node, nodes visited, and time
    

#As the name suggests, this method prints the required moves to console.
def printMoves(finalNode, method):
    stack = []
    currentNode = finalNode
    count = 0
    #I capped the moves at 100 to stop it from overwhelming the screen. In practice, this only affects DFS.
    while(currentNode._parent != None) and (count < 100):
        count = count + 1
        stack.append(currentNode._moved)
        currentNode = currentNode._parent
    stack.append(currentNode._moved)
    
    print(method)
    for i in range(len(stack)):
        print(f"Move {i}: {stack.pop()}")
    if(count == 100): 
        print("There are more than 100 moves. Printing will now stop.")
        
    
import random
#Creates a random board for the 2D array. May not always be solvable. 
def randomBoard():
    tempArray = [0, 1,2,3,4,5,6,7,8]
    outArray = [[0 for i in range(3)] for j in range(3)]
    
    for i in range(3):
        for j in range(3):
            temp = random.randint(0,100)%len(tempArray)
            outArray[i][j] = tempArray[temp]
            tempArray.pop(temp)
            
    return outArray


#Premade arrays, used for testing and examples.
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










######EVERYTHING BELOW IS GUI PLEASE NOTE I AM NOT GOOD AT IT##############


#Import tkinter library
from tkinter import *
from matplotlib import pyplot as plt
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
#NDC

#Create an instance of Tkinter frame or window
window = Tk()
fig = Figure(figsize = (5, 5),dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = window)  

#labels for the GUI
labelOne = Label(window, text="Current Starting Board:    ", font=("Times",36)).place(x=300,y=200)
labelTwo = Label(window, text="Nodes visited when solving with DFS: ", font=("Times",14)).place(x=850,y=150)
labelThree = Label(window, text="Nodes visited when solving with UCS: ", font=("Times",14)).place(x=850,y=300)
labelFour = Label(window, text="Nodes visited when solving with BFS: ", font=("Times",14)).place(x=850,y=450)
labelFive = Label(window, text="Nodes visited when solving with A*: ", font=("Times",14)).place(x=850,y=600)
labelSix = Label(window, text="If DFS == 25001 OR IF UCS, BFS, A* == 200001 \n then the algorithm did not find a solution and stopped.", font=("Times",14)).place(x=400,y=700)
#labelFour = Label(window, text="TEMP LINE \n NDC TEMP LINE \n NDC TEMP LINE \n NDC TEMP LINE.\n NDC TEMP LINE \n TEMP LINE.", font=("Times",14)).place(x=850,y=600)

canvas.draw()
canvas.get_tk_widget().place(x=300,y=200)
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

#class used to pass values between functions; I doubt this is proper coding but it works.
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


#Plots a random game onto the board
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
    labelFive = Label(window, text="A list of moves will be outputted to console.   ", font=("Times",16)).place(x=400,y=50)

#Plots a nonrandom game onto the board (there are only four options here)
def plotNonRandomGame():
    tempCV = tempVals.currentVal%4
    #print(tempCV)
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
    labelFive = Label(window, text="A list of moves will be outputted to console.   ", font=("Times",16)).place(x=400,y=50)
    

#Solves with dfs, note the variables on the node creation. 
def solveWithDFS():
    DFSNode = node(None, tempVals.currentTiles, 0, -1, "Start Node")
    
    string = "Nodes visited, time when solving with DFS: \n\n"
    outNode, nodesVisited, ttt = DFSMethod(DFSNode)
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelTwo = Label(window, text=string, font=("Times",14)).place(x=850,y=150)
    printMoves(outNode, "Using DFS")
    labelFive = Label(window, text="A list of moves for DFS outputted to console.   ", font=("Times",16)).place(x=400,y=50)
    

#Solves with UCS, note the variables on the node creation. This is how it distinguishes between the 3.
def solveWithUCS():
    UCSNode = node(None, tempVals.currentTiles, 0, 0, "Start Node")  #Create node
    
    string = "Nodes visited, time when solving with UCS: \n\n"
    outNode, nodesVisited, ttt = UCSMethod(UCSNode) #return values
    string = string + str(nodesVisited) + ", t = " + str(ttt) #Print nodes visited and time
    
    labelThree = Label(window, text=string, font=("Times",14)).place(x=850,y=300)
    printMoves(outNode, "Using UCS") #outputs solution to console
    labelFive = Label(window, text="A list of moves for UCS outputted to console.   ", font=("Times",16)).place(x=400,y=50)

    
#Solves with UCS, note the variables on the node creation. This is how it distinguishes between the 3.
def solveWithBFS():
    BFSNode = node(None, tempVals.currentTiles, -1, evalHN(tempVals.currentTiles), "Start Node")
    
    string = "Nodes visited, time when solving with BFS: \n\n"
    outNode, nodesVisited, ttt = BFSMethod(BFSNode)
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelFour = Label(window, text=string, font=("Times",14)).place(x=850,y=450)
    printMoves(outNode, "Using BFS")
    labelFive = Label(window, text="A list of moves for BFS outputted to console.   ", font=("Times",16)).place(x=400,y=50)
    

#Solves with UCS, note the variables on the node creation. This is how it distinguishes between the 3.
def solveWithAStar():
    aStarNode = node(None, tempVals.currentTiles, 0, evalHN(tempVals.currentTiles), "Start Node")
    outNode, nodesVisited, ttt = AStarMethod(aStarNode)
    string = "Nodes visited, time when solving with A*: \n\n"
    string = string + str(nodesVisited) + ", t = " + str(ttt)
    
    labelFive = Label(window, text=string, font=("Times",14)).place(x=850,y=600)
    printMoves(outNode, "Using A*")
    labelFive = Label(window, text="A list of moves for A* outputted to console.   ", font=("Times",16)).place(x=400,y=50)
    
    
#Buttons used on the program
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

#This makes the program work!
window.bind('<Return>',lambda event:callback())
window.mainloop()
presetList.append(arrayFour)
