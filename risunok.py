from graphics import *
from math import *

win = GraphWin("Test1", 820, 680)	#create window of size 300x300

a=pi/10

def preobras_koord(x, y):
    x01=x
    y01=y
    x=x01*cos(a)-y01*sin(a)
    y=x01*sin(a)+y01*cos(a)
    return x, y
    
    
def RT(x1, y1, x2, y2, col):
    L = Rectangle(Point(x1, y1), Point(x2, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)

def TRI(x1, y1, x2, y2, x3, y3, col):
    
    L = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)
    
def ELL(x1, y1, x2, y2, col):
       
    L = Oval(Point(x1, y1), Point(x2, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)

def RT1(x1, y1, x2, y2, col):
    x01=x1
    x02=x2
    
    y01=y1
    y02=y2
    
    x1, y1 = preobras_koord(x01, y01)
    
    x2, y2 = preobras_koord(x02, y02)
    
    L = Rectangle(Point(x1, y1), Point(x2, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)

def TRI1(x1, y1, x2, y2, x3, y3, col):
    x01=x1
    x02=x2
    x03 = x3
    y03 = y3
    
    y01=y1
    y02=y2
    
    
    
    x1, y1 = preobras_koord(x01, y01)
    
    x2, y2 = preobras_koord(x02, y02)
    
    x3, y3 = preobras_koord(x03, y03)
    
    L = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)
    
def ELL1(x1, y1, x2, y2, col):
    x01=x1
    x02=x2
    
    y01=y1
    y02=y2
    
    x1, y1 = preobras_koord(x01, y01)
    
    x2, y2 = preobras_koord(x02, y02)
     
    L = Oval(Point(x1, y1), Point(x2, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)

def POL(x1, y1, x2, y2, col):
    
    L=Polygon(Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)    

def POL1(x1, y1, x2, y2, col):
    x01=x1
    x02=x2
    
    y01=y1
    y02=y2
    
    x1, y1 = preobras_koord(x01, y01)
    
    x2, y2 = preobras_koord(x02, y02)
    
    x3, y3 = preobras_koord(x01, y02)
    
    x4, y4 = preobras_koord(x02, y01)
    
    L=Polygon(Point(x1, y1), Point(x3, y3), Point(x2, y2), Point(x4, y4))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)    

def podobie_sun(x,y,p):
    p=p/100
    ELL(x+p*30, y+p*30, x+p*130, y+p*130, "#FFFF00") #Солнце
    for i in range(0, 10):
        L = Line(Point(x+p*(80+75*cos(i*2*pi/10)), y+p*(80+75*sin(i*2*pi/10))), Point(x+p*(80+130*cos(i*2*pi/10)), y+p*(80+130*sin(i*2*pi/10))))
        if (i % 2 == 1): 
            L.setOutline("yellow")
        else: 
            L.setOutline("black")
        L.setWidth(5)
        L.draw(win)    

def podobie_chel(x,y,p):
    p=p/100
    
    ELL(x+p*100,y+p*100,x+p*150,y+p*150,"#FFFF00")
    L=Line(Point(x+p*125,y+p*150), Point(x+p*125,y+p*350))
    L.setOutline("black")
    L.setWidth(10)
    L.draw(win)
    
    L=Line(Point(x+p*125,y+p*200), Point(x+p*175,y+p*150))
    L.setOutline("black")
    L.setWidth(10)
    L.draw(win)
    
    L=Line(Point(x+p*125,y+p*200), Point(x+p*75,y+p*150))
    L.setOutline("black")
    L.setWidth(10)
    L.draw(win)
    
    L=Line(Point(x+p*125,y+p*350), Point(x+p*175,y+p*400))
    L.setOutline("black")
    L.setWidth(10)
    L.draw(win)
    
    L=Line(Point(x+p*125,y+p*350), Point(x+p*75,y+p*400))
    L.setOutline("black")
    L.setWidth(10)
    L.draw(win)
    
    

def podobie_house(x,y,p):
    p=p/100
    #Прямоугольники на рисунке
    #RT(p*0, p*0, p*820, p*680, "#1E90FF") #Небо
    #RT(p*0, p*570, p*820, p*680, "#ADFF2F") #Трава
    POL1(x+p*100, y+p*320, x+p*400, y+p*600, "#FF8C00") #Основная стена
    POL1(x+p*100, y+p*530, x+p*400, y+p*600, "#B22222") #Фундамент
    POL1(x+p*400, y+p*440, x+p*490, y+p*600, "#FFA500") #Пристройка
    POL1(x+p*310, y+p*225, x+p*360, y+p*320, "#B22222") #Труба
    POL1(x+p*410, y+p*480, x+p*470, y+p*600, "#8B4513") #Дверь
    POL1(x+p*263, y+p*340, x+p*373, y+p*505, "#00FFFF") #Правое окно2
    POL1(x+p*127, y+p*340, x+p*237, y+p*505, "#00FFFF") #Левое окно
    #RT(660, 340, 720, 600, "#800000") #Ствол50
        
    #Треугольники на рисунке
    TRI1(x+p*80, y+p*320, x+p*250, y+p*200, x+p*420, y+p*320, "#FF4500") #Главная крыша
    TRI1(x+p*400, y+p*370, x+p*400, y+p*440, x+p*490, y+p*440, "#FF4500") #Крыша пристройки
    
    
def podobie_house0(x,y,p):
    p=p/100
    #Прямоугольники на рисунке
    #RT(p*0, p*0, p*820, p*680, "#1E90FF") #Небо
    #RT(p*0, p*570, p*820, p*680, "#ADFF2F") #Трава
    POL(x+p*100, y+p*320, x+p*400, y+p*600, "#FF8C00") #Основная стена
    POL(x+p*100, y+p*530, x+p*400, y+p*600, "#B22222") #Фундамент
    POL(x+p*400, y+p*440, x+p*490, y+p*600, "#FFA500") #Пристройка
    POL(x+p*310, y+p*225, x+p*360, y+p*320, "#B22222") #Труба
    POL(x+p*410, y+p*480, x+p*470, y+p*600, "#8B4513") #Дверь
    POL(x+p*263, y+p*340, x+p*373, y+p*505, "#00FFFF") #Правое окно2
    POL(x+p*127, y+p*340, x+p*237, y+p*505, "#00FFFF") #Левое окно
    #RT(660, 340, 720, 600, "#800000") #Ствол50
        
    #Треугольники на рисунке
    TRI(x+p*80, y+p*320, x+p*250, y+p*200, x+p*420, y+p*320, "#FF4500") #Главная крыша
    TRI(x+p*400, y+p*370, x+p*400, y+p*440, x+p*490, y+p*440, "#FF4500") #Крыша пристройки

        
    
    
def podobie_tree(x,y,p):
    p=p/100
    RT(x+p*660, y+p*340, x+p*720, y+p*600, "#800000") #Ствол
    ELL(x+p*590, y+p*330, x+p*750, y+p*400, "#ADFF2F") #Крона 1
    ELL(x+p*570, y+p*170, x+p*800, y+p*370, "#008000") #Крона 2
    ELL(x+p*580, y+p*180, x+p*650, y+p*217, "#ADFF2F") #Крона 3
    ELL(x+p*700, y+p*396, x+p*790, y+p*450, "#ADFF2F") #Крона 4
    ELL(x+p*572, y+p*428, x+p*685, y+p*506, "#008000") #Крона 5    

def podobie_oblach(x,y,p):
    p=p/100
    ELL(x+p*326, y+p*176, x+p*394, y+p*212, "#C0C0C0") #Дым 1
    ELL(x+p*367, y+p*130, x+p*475, y+p*180, "#C0C0C0") #Дым 2
    ELL(x+p*440, y+p*74, x+p*575, y+p*138, "#C0C0C0") #Дым 3    

#Прямоугольники на рисунке

RT(0, 0, 820, 680, "#1E90FF") #Небо
RT(0, 570, 820, 680, "#ADFF2F") #Трава



podobie_house0(0,0,100)

podobie_tree(0,0,100)

podobie_sun(0,0,100)

podobie_oblach(0,0,100)


podobie_tree(100,100,40)


podobie_house(200,300,40)


podobie_oblach(0,0,50)


podobie_sun(200,100,20)


podobie_chel(300,400,50)
#Лучики

win.getMouse()
win.close()