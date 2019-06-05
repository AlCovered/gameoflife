import random
import time
import os

#Position has three parameters: x, y, is the cell alive

class Point(object):
    def __init__(self,isAlive,x,y):
        self.isAlive = isAlive
        self.x = x
        self.y = y
    def GetPoint(self):
        return self.x,self.y
    def isAlive(self):
        return self.isAlive
    def Set(self,isAlive):
        self.isAlive = isAlive

#This function checks the end of game condition

def testSystem(Array):
    result = False
    for i in range(len(Array)):
        if Array[i].isAlive == True:
            result = True
            break
    return result

#This function checks if the point is on the cut

def test(WorldWidth,i):
    while WorldWidth<=i:
        i-=i
    if i==WorldWidth:
        return True
    else:
        return False

#This function counts the number of living neighbors

def get(i,Array,WorldWidth,WorldHeight,Name):
    result = 0
    if Name:
        result+=get(i-1,Array,WorldWidth,WorldHeight,False)
        result+=get(i+1,Array,WorldWidth,WorldHeight,False)
        result+=get(i-1-WorldWidth,Array,WorldWidth,WorldHeight,False)
        result+=get(i+1-WorldWidth,Array,WorldWidth,WorldHeight,False)
        result+=get(i-1+WorldWidth,Array,WorldWidth,WorldHeight,False)
        result+=get(i+1+WorldWidth,Array,WorldWidth,WorldHeight,False)
        result+=get(i+WorldWidth,Array,WorldWidth,WorldHeight,False)
        result+=get(i-WorldWidth,Array,WorldWidth,WorldHeight,False)
    else:
        if(i<0 or i>=WorldWidth*WorldHeight):
            return 0
        if i == 0:
            if Array[i].isAlive:
                return 1
            else:
                return 0
        if(test(WorldWidth,i)):
            return 0
        if Array[i].isAlive:
            return 1
        else:
            return 0
    return result

#Just draw our world

def draw(Array,WorldWidth):
    numStr = 0
    for i in range(len(Array)):
        if Array[i].isAlive:
            print("*",end="")
        else:
            print(" ",end="")
        if i+1-numStr*WorldWidth == WorldWidth:
            print()
            numStr+=1
    #print("--------------------")


def checkConfiguration(ArrayGap,ArrayConf):
    result = True
    for i in range(len(ArrayGap)):
        if ArrayConf[i]!=ArrayGap[i]:
            result = False
            break
    return result
#Main function
            
if __name__ == "__main__":
    
    #clear for our console
    
    ArrayConf = []
    clear = lambda: os.system('cls')
    Array = []
    
    #You can set Height and Width and StartLifeNum
    
    WorldHeight = 20
    WorldWidth = 20
    StartLifeNum = 100
    
    for i in range(WorldHeight):
        for j in range(WorldWidth):
            Array.append(Point(False,i,j))
    
    #Positions for Glider (for scene 20*20)
    
    """
    Array[10].Set(True)
    Array[10].Set(True)
    Array[21].Set(True)
    Array[22].Set(True)
    Array[12].Set(True)
    Array[2].Set(True)
    """

    #Positions for Configuration (for scene 10*10)
    
    """
    Array[0].Set(True)
    Array[1].Set(True)
    Array[10].Set(True)
    Array[11].Set(True)
    """
    
    #random positions
    
    for i in range(StartLifeNum):
        x,y = random.choice(Array).GetPoint()
        if Array[x*WorldWidth+y].isAlive:
            i-=1
        else:
            Array[x*WorldWidth+y].Set(True)
    
    """
    for i in Array:
        print(i.GetPoint(),i.isAlive)
    """

    #Our Game Life
    
    for i in Array:
        ArrayConf.append(i.isAlive)
    while testSystem(Array):
        clear()
        draw(Array,WorldWidth)
        ArrayGap = []
        for i in range(len(Array)):
            NumPoints = get(i,Array,WorldWidth,WorldHeight,True)
            #print(i,NumPoints)
            if Array[i].isAlive:
                if NumPoints < 2 or NumPoints > 3:
                    ArrayGap.append(False)
                else:
                    ArrayGap.append(True)
            else:
                 if NumPoints == 3:
                    ArrayGap.append(True)
                 else:
                     ArrayGap.append(False)
        if checkConfiguration(ArrayGap,ArrayConf):
            break
        ArrayConf = []
        for i in range(len(ArrayGap)):
            ArrayConf.append(ArrayGap[i])
            if ArrayGap[i]:
                Array[i].Set(True)
            else:
                Array[i].Set(False)
        time.sleep(0.05)
    print("Civilization is over...")
    time.sleep(100)
