from graphics import *

win = GraphWin("Tiger", 1200, 1000)
Jungle = Image(Point(600, 500), "Jungle.png")
Jungle.draw(win)
class BoardSpace:
    def __init__(self, circle, circleNum):
        self.circle = circle
        self.circleNum = circleNum
        self.tigerImage = Image(circle.getCenter(), "Tiger.png")
        self.lambImage = Image(circle.getCenter(), "Lamb.png")
        self.lambT = False
        self.tigerT = False
        self.adjSpaces = []
    
    def drawCircle(self):
        self.circle.setFill('red')
        self.circle.setOutline('white')
        self.circle.setWidth(5)
        self.circle.draw(win)
    
    def setFill(self, color):
        self.circle.setFill(color)
    
    def drawTiger(self):
        self.tigerT = True
        self.tigerImage.draw(win)
    
    def undrawTiger(self):
        self.tigerT = False
        self.tigerImage.undraw()
        
    def drawLamb(self):
        self.lambT = True
        self.lambImage.draw(win)
    
    def undrawLamb(self):
        self.lambT = False
        self.lambImage.undraw()
    
    def setAdjSpaces(self, spaces):
        self.adjSpaces = spaces
        
    def getCenter(self):
        return self.circle.getCenter()
    
    def getX1(self):
        return self.circle.getCenter().getX() - self.circle.getRadius()
    
    def getX2(self):
        return self.circle.getCenter().getX() + self.circle.getRadius()
    
    def getY1(self):
        return self.circle.getCenter().getY() - self.circle.getRadius()
    
    def getY2(self):
        return self.circle.getCenter().getY() + self.circle.getRadius()
    
    def getLambT(self):
        return self.lambT
    
    def setLambT(self, lambT):
        self.lambT = lambT
    
    def getTigerT(self):
        return self.tigerT
    
    def setTigerT(self, tigerT):
        self.tigerT = tigerT
        
    def getAnimalT(self):
        return (self.tigerT or self.lambT)
        
    def getAdjSpaces(self):
        return self.adjSpaces
        
    def setAdjSpaces(self, adjSpaces):
        self.adjSpaces = adjSpaces
        
    def getCircleNum(self):
        return self.circleNum
    

def getCircleLoc(CP):
    global Circle1
    global Circle2
    global Circle3
    global Circle4
    global Circle5
    global Circle6
    global Circle7
    global Circle8
    global Circle9
    global Circle10
    global Circle11
    global Circle12
    global Circle13
    global Circle14
    global Circle15
    global Circle16
    global Circle17
    
    if (CP.getX() >= Circle1.getX1() and CP.getX() <= Circle1.getX2() and CP.getY() >= Circle1.getY1() and CP.getY() <= Circle1.getY2()):
        return 1
    
    elif (CP.getX() >= Circle2.getX1() and CP.getX() <= Circle2.getX2() and CP.getY() >= Circle2.getY1() and CP.getY() <= Circle2.getY2()):
        return 2
    
    elif (CP.getX() >= Circle3.getX1() and CP.getX() <= Circle3.getX2() and CP.getY() >= Circle3.getY1() and CP.getY() <= Circle3.getY2()):
        return 3
    
    elif (CP.getX() >= Circle4.getX1() and CP.getX() <= Circle4.getX2() and CP.getY() >= Circle4.getY1() and CP.getY() <= Circle4.getY2()):
        return 4
    
    elif (CP.getX() >= Circle5.getX1() and CP.getX() <= Circle5.getX2() and CP.getY() >= Circle5.getY1() and CP.getY() <= Circle5.getY2()):
        return 5
    
    elif (CP.getX() >= Circle6.getX1() and CP.getX() <= Circle6.getX2() and CP.getY() >= Circle6.getY1() and CP.getY() <= Circle6.getY2()):
        return 6
    
    elif (CP.getX() >= Circle7.getX1() and CP.getX() <= Circle7.getX2() and CP.getY() >= Circle7.getY1() and CP.getY() <= Circle7.getY2()):
        return 7
    
    elif (CP.getX() >= Circle8.getX1() and CP.getX() <= Circle8.getX2() and CP.getY() >= Circle8.getY1() and CP.getY() <= Circle8.getY2()):
        return 8
    
    elif (CP.getX() >= Circle9.getX1() and CP.getX() <= Circle9.getX2() and CP.getY() >= Circle9.getY1() and CP.getY() <= Circle9.getY2()):
        return 9
    
    elif (CP.getX() >= Circle10.getX1() and CP.getX() <= Circle10.getX2() and CP.getY() >= Circle10.getY1() and CP.getY() <= Circle10.getY2()):
        return 10
    
    elif (CP.getX() >= Circle11.getX1() and CP.getX() <= Circle11.getX2() and CP.getY() >= Circle11.getY1() and CP.getY() <= Circle11.getY2()):
        return 11
    
    elif (CP.getX() >= Circle12.getX1() and CP.getX() <= Circle12.getX2() and CP.getY() >= Circle12.getY1() and CP.getY() <= Circle12.getY2()):
        return 12
    
    elif (CP.getX() >= Circle13.getX1() and CP.getX() <= Circle13.getX2() and CP.getY() >= Circle13.getY1() and CP.getY() <= Circle13.getY2()):
        return 13
    
    elif (CP.getX() >= Circle14.getX1() and CP.getX() <= Circle14.getX2() and CP.getY() >= Circle14.getY1() and CP.getY() <= Circle14.getY2()):
        return 14
    
    elif (CP.getX() >= Circle15.getX1() and CP.getX() <= Circle15.getX2() and CP.getY() >= Circle15.getY1() and CP.getY() <= Circle15.getY2()):
        return 15
    
    elif (CP.getX() >= Circle16.getX1() and CP.getX() <= Circle16.getX2() and CP.getY() >= Circle16.getY1() and CP.getY() <= Circle16.getY2()):
        return 16
    
    elif (CP.getX() >= Circle17.getX1() and CP.getX() <= Circle17.getX2() and CP.getY() >= Circle17.getY1() and CP.getY() <= Circle17.getY2()):
        return 17
    
    else:
        return 0

def checkGame(LambList, TigerList):
    global CircleList
    global LambsLeft
    if (len(LambList) + LambsLeft < 4):
        return False
    
    for i in range(len(TigerList)):
        myCircleAdj = TigerList[i].getAdjSpaces()
        
        for j in range(len(myCircleAdj[0])):
            if (myCircleAdj[1][j] == 0):
                continue
            
            elif (CircleList[myCircleAdj[0][j] - 1].getLambT() == True and CircleList[myCircleAdj[1][j] - 1].getLambT() == False and CircleList[myCircleAdj[1][j] - 1].getTigerT() == False):
                return True
    
        for k in range(len(myCircleAdj[0])):
            if (CircleList[myCircleAdj[0][k] - 1].getLambT() == True or CircleList[myCircleAdj[0][k] - 1].getTigerT() == True):
                continue
            
            else:
                return True
            
    return False
           

CircleSize = 35

Circle1 = BoardSpace(Circle(Point(600, 300), CircleSize), 1)
Circle2 = BoardSpace(Circle(Point(270, 500), CircleSize), 2)
Circle3 = BoardSpace(Circle(Point(430, 500), CircleSize), 3)
Circle4 = BoardSpace(Circle(Point(543, 500), CircleSize), 4)
Circle5 = BoardSpace(Circle(Point(657, 500), CircleSize), 5)
Circle6 = BoardSpace(Circle(Point(770, 500), CircleSize), 6)
Circle7 = BoardSpace(Circle(Point(930, 500), CircleSize), 7)
Circle8 = BoardSpace(Circle(Point(50, 700), CircleSize), 8)
Circle9 = BoardSpace(Circle(Point(270, 700), CircleSize), 9)
Circle10 = BoardSpace(Circle(Point(490, 700), CircleSize), 10)
Circle11 = BoardSpace(Circle(Point(710, 700), CircleSize), 11)
Circle12 = BoardSpace(Circle(Point(930, 700), CircleSize), 12)
Circle13 = BoardSpace(Circle(Point(1150, 700), CircleSize), 13)
Circle14 = BoardSpace(Circle(Point(100, 900), CircleSize), 14)
Circle15 = BoardSpace(Circle(Point(433, 900), CircleSize), 15)
Circle16 = BoardSpace(Circle(Point(766, 900), CircleSize), 16)
Circle17 = BoardSpace(Circle(Point(1100, 900), CircleSize), 17)

CircleList = [Circle1, Circle2, Circle3, Circle4, Circle5, Circle6, Circle7, Circle8, Circle9, Circle10, Circle11, Circle12, Circle13, Circle14, Circle15, Circle16, Circle17]

Line1 = Line(Circle1.getCenter(), Circle14.getCenter())
Line2 = Line(Circle1.getCenter(), Circle15.getCenter())
Line3 = Line(Circle1.getCenter(), Circle16.getCenter())
Line4 = Line(Circle1.getCenter(), Circle17.getCenter())
Line5 = Line(Circle2.getCenter(), Circle8.getCenter())
Line6 = Line(Circle7.getCenter(), Circle13.getCenter())
Line7 = Line(Circle2.getCenter(), Circle7.getCenter())
Line8 = Line(Circle8.getCenter(), Circle13.getCenter())

LineList = [Line1, Line2, Line3, Line4, Line5, Line6, Line7, Line8]
for i in LineList:
    i.setWidth(5)
    i.setOutline('black')
    i.draw(win)

for i in CircleList:
    i.drawCircle()

InstructText = Text(Point(600, 150), '')
InstructText.setSize(24)
InstructText.setStyle('bold')
InstructText.setTextColor('black')
InstructText.draw(win)

LambList = []
TigerList = []

for i in range(3):
    NoOptionPicked = True
    InstructStr = "Puli(Tiger) Player! Place down " + str(3 - i) + " more Puligal(tigers)!"
    InstructText.setText(InstructStr)
    while(NoOptionPicked):
        CP = win.getMouse()
        CL = getCircleLoc(CP)
        if (CL != 0):
            myCircle = CircleList[CL - 1]
            if (myCircle.getTigerT() == False):
                myCircle.drawTiger()
                TigerList.append(myCircle)
                NoOptionPicked = False
            
Circle1.setAdjSpaces([[3, 4, 5, 6], [9, 10, 11, 12]])
Circle2.setAdjSpaces([[3, 8], [4, 0]])
Circle3.setAdjSpaces([[1, 2, 4, 9], [0, 0, 5, 14]])
Circle4.setAdjSpaces([[1, 3, 5, 10], [0, 2, 6, 15]])
Circle5.setAdjSpaces([[1, 4, 6, 11], [0, 3, 7, 16]])
Circle6.setAdjSpaces([[1, 5, 7, 12], [0, 4, 0, 17]])
Circle7.setAdjSpaces([[6, 13], [5, 0]])
Circle8.setAdjSpaces([[2, 9], [0, 10]])
Circle9.setAdjSpaces([[3, 8, 10, 14], [1, 0, 11, 0]])
Circle10.setAdjSpaces([[4, 9, 11, 15], [1, 8, 12, 0]])
Circle11.setAdjSpaces([[5, 10, 12, 16], [1, 9, 13, 0]])
Circle12.setAdjSpaces([[6, 11, 13, 17], [1, 10, 0, 0]])
Circle13.setAdjSpaces([[7, 12], [0, 11]])
Circle14.setAdjSpaces([[9], [3]])
Circle15.setAdjSpaces([[10], [4]])
Circle16.setAdjSpaces([[11], [5]])
Circle17.setAdjSpaces([[12], [6]])

PlayerTurn = 1;
LambsLeft = 14;
myCircle = Circle1

while(checkGame(LambList, TigerList)):
    if (PlayerTurn == 1): #Lamb's Turn
        InstructText.setTextColor('black')
        if (LambsLeft > 0): #Need to Place Down Lambs
            NoOptionPicked = True
            InstructStr = "Aadu(Lamb) Player! Place down an Aadu, you have " + str(LambsLeft) + " remaining"
            InstructText.setText(InstructStr)
            while (NoOptionPicked):
                CP = win.getMouse()
                CL = getCircleLoc(CP)
                if (CL != 0):
                    myCircle = CircleList[CL - 1]
                    if (myCircle.getLambT() == False and myCircle.getTigerT() == False):
                        myCircle.drawLamb()
                        LambList.append(myCircle)
                        NoOptionPicked = False
                        LambsLeft -= 1
        
        else: #Move Lambs
            TurnComplete = False
            InstructStr = "Aadu Player! Move one of your Aadu!"
            InstructText.setText(InstructStr)
            while (TurnComplete == False):
                NoOptionPicked = True
                while (NoOptionPicked):
                    CP = win.getMouse()
                    CL = getCircleLoc(CP)
                    if (CL != 0):
                        myCircle = CircleList[CL - 1]
                        if (myCircle.getLambT() == True and myCircle.getTigerT() == False):
                            NoOptionPicked = False
                            myCircle.setFill('blue')
                            
                
                CP = win.getMouse()
                CL = getCircleLoc(CP)
                if (CL != 0):
                    myCircle2 = CircleList[CL - 1]
                    if (myCircle2.getLambT() == False and myCircle2.getTigerT() == False):
                        myCircleAdj = myCircle.getAdjSpaces()
                        if (myCircle2.getCircleNum() in myCircleAdj[0]):
                            myCircle.undrawLamb()
                            LambList.remove(myCircle)
                            myCircle2.drawLamb()
                            LambList.append(myCircle2)
                            TurnComplete = True
                
                myCircle.setFill('red')
                
        PlayerTurn = 2
    
    else: #Tiger Turn
        TurnComplete = False
        InstructStr = "Puli Player! Move a Puli or jump over an Aadu!"
        InstructText.setTextColor('Black')
        InstructText.setText(InstructStr)
        while (TurnComplete == False):
            NoOptionPicked = True
            while (NoOptionPicked):
                CP = win.getMouse()
                CL = getCircleLoc(CP)
                if (CL != 0):
                    myCircle = CircleList[CL - 1]
                    if (myCircle.getLambT() == False and myCircle.getTigerT() == True):
                        NoOptionPicked = False
                        myCircle.setFill('blue')
                        
            myCircleAdj = myCircle.getAdjSpaces()
            CP = win.getMouse()
            CL = getCircleLoc(CP)
            if (CL != 0):
                myCircle2 = CircleList[CL - 1]
                if (myCircle2.getTigerT() == False and myCircle2.getLambT() == False):
                    if (myCircle2.getCircleNum() in myCircleAdj[0]):
                        myCircle.undrawTiger()
                        TigerList.remove(myCircle)
                        myCircle2.drawTiger()
                        TigerList.append(myCircle2)
                        TurnComplete = True
                    
                    elif (myCircle2.getCircleNum() in myCircleAdj[1]):
                        jumpIndex = myCircleAdj[1].index(myCircle2.getCircleNum())
                        adjCircleNum = myCircleAdj[0][jumpIndex]
                        adjCircle = CircleList[adjCircleNum - 1]
                        if (adjCircle.getLambT() == True):
                            myCircle.undrawTiger()
                            TigerList.remove(myCircle)
                            adjCircle.undrawLamb()
                            LambList.remove(adjCircle)
                            myCircle2.drawTiger()
                            TigerList.append(myCircle2)
                            TurnComplete = True
            
            myCircle.setFill('red')
        PlayerTurn = 1
                        
if (len(LambList) + LambsLeft < 4):
    InstructText.setText('Puli Player Wins!')
else:
    InstructText.setText('Aadu Player Wins!')
    
    
        