from graphics import *
from math import *
from random import *


height=700
width=height

win = GraphWin("Test1", height, width )

R=3
r=1

b = randint(-2*R+4, 2*R-4)

dT = 0.01

Vox = randint(1000,1000)
Voy = 0

Uox = 0
Uoy = 0

Xo = 50
Yo = height/2

X1 = width/2
Y1 = height/2 + b

Cir1 = Circle(Point(Xo,Yo), R)
Cir2 = Circle(Point(X1,Y1), R)

Cir1.setFill("black")
Cir2.setFill("brown")

Cir1.draw(win)
Cir2.draw(win)


si = abs(b)/(2*R)
co = (1 - si**2)**0.5

def lev_stenka(x):
    if x-R < 0: 
        flag = 0
    else:
        flag = 1
    return flag

def prav_stenka(x):
    if x+R > width: 
        flag = 0
    else:
        flag = 1
    return flag

def verh_stenka(y):
    if y-R < 0: 
        flag = 0
    else:
        flag = 1
    return flag

def nizh_stenka(y):
    if y+R > height: 
        flag = 0
    else:
        flag = 1
    return flag

j = 0
while ((Xo - X1)**2 + (Yo - Y1)**2)**0.5 > 2*R:
    Xo = Xo + Vox * dT
    Cir1.move(Vox * dT, 0)
    time.sleep(dT)
    if j % 1 == 0:
        C = Circle(Point(Xo,Yo), r)
        C.setFill("black")
        C.draw(win)
    j = j+1
    
    
V = Vox

if b > 0:
    Vox = V * si*2 
    Voy = - V * co * si
    
    Uox = V * co**2
    Uoy = V * co * si
else:
    Vox = V * si*2 
    Voy = V * co * si
    
    Uox = V * co**2
    Uoy = - V * co * si 
    
i = 0

while 1==1:
    if verh_stenka(Yo)*nizh_stenka(Yo)*prav_stenka(Xo)*lev_stenka(Xo) == 0:
        Vox = 0
        Voy = 0
    if verh_stenka(Y1)*nizh_stenka(Y1)*prav_stenka(X1)*lev_stenka(X1) == 0:
        Uox = 0
        Uoy = 0
    
    if i % 1 == 0:
        C = Circle(Point(Xo,Yo), r)
        Ci = Circle(Point(X1,Y1), r)
        
        C.setFill("black")
        Ci.setFill("brown")
        
        C.draw(win)
        Ci.draw(win)  
    
    i = i+1
    
    Xo = Xo + Vox * dT
    Yo = Yo + Voy * dT 
    
    X1 = X1 + Uox * dT
    Y1 = Y1 + Uoy * dT
    
    Cir1.move(Vox * dT, Voy * dT)  
    Cir2.move(Uox * dT, Uoy * dT)
  
    
    time.sleep(dT)