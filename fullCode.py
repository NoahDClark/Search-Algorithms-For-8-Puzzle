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

