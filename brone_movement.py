from graphics import *
from math import *
from array import *
from random import *


height=400
width=height

win = GraphWin("Test1", height, width )

L=Line(Point(1, 0), Point(1,height))
L2=Line(Point(width-1, 0), Point(width-1, height))
L.draw(win)
L2.draw(win)


Xo=width/10
Yo=height/2

X1=width/2
Y1=height/2

Vox=-200
Voy=-105

Uox=2000
Uoy=100

dT=0.002

r=10
R=20

k=1000

N=5
 

Cc = []
CcVx = []
CcVy = []

CcX = []
CcY = []



def lev_stenka(x):
    if x-r < 0: 
        flag = 0
    else:
        flag = 1
    return flag

def prav_stenka(x):
    if x+r > width: 
        flag = 0
    else:
        flag = 1
    return flag

def verh_stenka(y):
    if y-r < 0: 
        flag = 0
    else:
        flag = 1
    return flag

def nizh_stenka(y):
    if y+r > height: 
        flag = 0
    else:
        flag = 1
    return flag

for i in range(N):
    X1 = randint(0,width)
    Y1 = randint(0,height)
    
    Vx = randint (100, 150)
    Vy = randint (100, 150)
    
    CcVx.append(Vx)
    CcVy.append(Vy)
    
    CcX.append(X1)
    CcY.append(Y1)
    
    C1=Circle(Point(X1, Y1), r)
    C1.setFill("black")
    
    
    Cc.append(C1)
    
    Cc[i].draw(win)
    



while 1==1:
    for i in range(N):
        
        for j in range(N):
            
            if i != j:
                
                if nizh_stenka(CcY[i])*verh_stenka(CcY[i]) == 0:
                    CcVy[i] = -CcVy[i]
                
                if lev_stenka(CcX[i])*prav_stenka(CcX[i]) == 0:
                    CcVx[i]= -CcVx[i]        
                
                if nizh_stenka(CcY[j])*verh_stenka(CcY[j]) == 0:
                    CcVy[j]= -CcVy[j]
                
                if lev_stenka(CcX[j])*prav_stenka(CcX[j]) == 0:
                    CcVx[j]= -CcVx[j]        
                
                if abs(CcX[i] - CcX[j]) < 2*r and abs(CcY[i] - CcY[j]) < 2*r:
                    CcVx[i], CcVx[j] = CcVx[j], CcVx[i]
                    CcVy[i], CcVy[j] = CcVy[j], CcVy[i]
    
           
        
                CcY[i]= CcY[i] + CcVy[i] * dT
                CcX[i] = CcX[i] + CcVx[i] * dT
                Cc[i].move(CcVx[i] * dT, CcVy[i] * dT)    
                    
                CcY[j]= CcY[j] + CcVy[j] * dT
                CcX[j] = CcX[j] + CcVx[j] * dT
                Cc[j].move(CcVx[j] * dT, CcVy[j] * dT)
    
    
    
    time.sleep(dT)    
    
           
    






win.getMouse()
win.close()