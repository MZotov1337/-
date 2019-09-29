from graphics import *
win = GraphWin("Wing", 400, 400)

def draw_house(x = 0, y = 0, k = 1, col = "yellow"):
    Pipe = Rectangle(Point(x+k*130, y+k*80), Point(x+k*160,y+k*140))
    Pipe.setFill("Black")
    Pipe.draw(win)
    
    House = Rectangle(Point(x+k*100, y+k*150), Point(x+k*300,y+k*250))
    House.setFill(col)
    House.draw(win)
    
    Roof = Polygon(Point(x+k*100,y+k*150), Point(x+k*300,y+k*150), Point(x+k*200,y+k*80))
    Roof.setFill("Red")
    Roof.draw(win)
    
    Door = Rectangle(Point(x+k*230,y+k*170), Point(x+k*270,y+k*240))
    Door.setFill("Black")
    Door.draw(win)
    
    Window = Rectangle(Point(x+k*125,y+k*175), Point(x+k*165, y+k*215))
    Window.setFill("White")
    Window.draw(win)
    
    Smoke1 = Oval(Point(x+k*130,y+k*80), Point(x+k*160,y+k*60))
    Smoke1.setFill("Grey")
    Smoke1.draw(win)
    
    Smoke2 = Oval(Point(x+k*140,y+k*70), Point(x+k*165,y+k*55))
    Smoke2.setFill("White")
    Smoke2.draw(win)
    
    Line1 = Line(Point(x+k*145, y+k*175), Point(x+k*145,y+k*215))
    Line1.draw(win)
    
    Line2 = Line(Point(x+k*125,y+k*195), Point(x+k*165,y+k*195))
    Line2.draw(win)
    
    Hand = Oval(Point(x+k*260,y+k*213), Point(x+k*265,y+k*220))
    Hand.setFill("White")
    Hand.draw(win)

def draw_sun():
    Sun1part = Polygon(Point(30,30), Point(80,30), Point(55,80))
    Sun1part.setFill("Yellow")

    Sun2part = Polygon(Point(55,17), Point(30,67.26), Point(80, 67.26))
    Sun2part.setFill("Yellow")

    Sun1part.setOutline("Yellow")
    Sun2part.setOutline("Yellow")

    Sun1part.draw(win)
    Sun2part.draw(win)
    

Grass = Rectangle(Point(0,210), Point(400,400))
Grass.setFill("Green")
Grass.draw(win)

Sky = Rectangle(Point(0,0), Point(400,210))
Sky.setFill("Light Blue")
Sky.draw(win)

PondSide = Oval(Point(142.9,285.7), Point(367.5,367.5))
PondSide.setFill("Yellow")
PondSide.draw(win)

Pond = Oval(Point(150,300), Point(350,350))
Pond.setFill("Blue")
Pond.draw(win)

draw_house()

win.getMouse()
win.close()