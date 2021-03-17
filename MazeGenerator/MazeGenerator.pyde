screenSize = [1920, 1080]



# from classes import Maze

class Maze:
    def __init__(self, sizeofBoard):
        self.size = sizeofBoard
        self.blocks = list()
        self.cellSize = 1000/sizeofBoard
        self.squareSize = self.cellSize*0.7
        
        self.padx = 485
        self.pady = 65
        
        for y in range(self.size):
            self.blocks.append([])
            for x in range(self.size):
            
                self.blocks[y].append([False for _ in range(4)])
                
    def isOpen (self, xindex, yindex):
        block = self.blocks[xindex][yindex]
        return any(block)

    def drawMaze(self):
        for xindex, column in enumerate(self.blocks):
            for yindex, block in enumerate(column):
                # rectMode(CENTER)
                fill(255)
                noStroke()
                
                square(xindex*self.cellSize+460+25, yindex*self.cellSize+40+25, self.squareSize)
                
    def dig(self, index, direction):
        if index[0] == 0 and direction==0:
            return False
        
        if index[1] == 0 and direction==3:
            return False
        
        if index[0] == self.size and direction==2:
            return False
        
        if index[1] == self.size and direction==1:
            return False
        
        self.drawBetweenCells(index, direction)
        neighbors = self.getNeighbors(index)
        index2 = neighbors[direction]
        
        fill(0,255,0)
        
        square(index[0]*self.cellSize+self.padx, index[1]*self.cellSize+self.pady, self.squareSize)
        square(index2[0]*self.cellSize+self.padx, index2[1]*self.cellSize+self.pady, self.squareSize)
        
        self.blocks[index[0]][index[1]][direction] = True
        self.blocks[index2[0]][index2[1]][self.getOppositeDirection(direction)] = True
        
        self.drawBetweenCells(index, direction)
        self.drawBetweenCells(index2, self.getOppositeDirection(direction))
        
        return True
        
    def getOppositeDirection(self, direction):
        if direction in [3,1]:
            return 4-direction
        
        return 2-direction
        
    def drawBetweenCells(self, index, direction):
        fill(0,255,0)
        noStroke()
        change = (100 - self.squareSize)/2
        
        if direction == 0:
            square(index[0]*self.cellSize+self.padx, index[1]*self.cellSize+self.pady+change, self.squareSize)
        
        if direction == 1:
            square(index[0]*self.cellSize+self.padx+change, index[1]*self.cellSize+self.pady, self.squareSize)
            
        if direction == 2:
            square(index[0]*self.cellSize+self.padx, index[1]*self.cellSize+self.pady-change, self.squareSize)
            
        if direction == 3:
            square(index[0]*self.cellSize+self.padx-change, index[1]*self.cellSize+self.pady, self.squareSize)
        
        

    def getNeighbors(self, index):
        
        indexofNeighbors = [None for _ in range(4)]
        
        if index[0] != 0:
            indexofNeighbors[0] = [index[0], index[1]+1]
        
        if index[1] != 0:
            indexofNeighbors[3] = [index[0]-1, index[1]]
        
        if index[0] != self.size:
            indexofNeighbors[1] = [index[0]+1, index[1]]
        
        if index[1] != self.size:
            indexofNeighbors[2] = [index[0], index[1]-1]
            
        return indexofNeighbors
    

theMaze = Maze(20)


def setup ():
    # size(1920, 1080);
    fullScreen(1)
    background(0, 0, 40);
    rectMode(CENTER);
    fill(0);
    stroke(255)
    strokeWeight(4)
    square(screenSize[0]/2, screenSize[1]/2, 1000);
    print(screenSize)
    theMaze.drawMaze()
    print("Digged:",theMaze.dig([19,19],2))
    print(theMaze.blocks[19][18])
    print(theMaze.isOpen(19,18))
    print(theMaze.isOpen(19,19))
    
    
def draw ():
    pass
    
    
def mousePressed():
    exit()
