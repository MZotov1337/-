from graphics import *
win = GraphWin("Wing", 400, 400)

Grass = Rectangle(Point(0,210), Point(400,400))
Grass.setFill("Green")
Grass.draw(win)

Sky = Rectangle(Point(0,0), Point(400,210))
Sky.setFill("Light Blue")
Sky.draw(win)


Pipe = Rectangle(Point(130, 80), Point(160,140))
Pipe.setFill("Black")
Pipe.draw(win)



House = Rectangle(Point(100, 150), Point(300,250))
House.setFill("Yellow")
House.draw(win)

Roof = Polygon(Point(100,150), Point(300,150), Point(200,80))
Roof.setFill("Red")
Roof.draw(win)

Door = Rectangle(Point(230,170), Point(270,240))
Door.setFill("Black")
Door.draw(win)

Window = Rectangle(Point(125,175), Point(165, 215))
Window.setFill("White")
Window.draw(win)

Line1 = Line(Point(145, 175), Point(145,215))
Line1.draw(win)

Line2 = Line(Point(125,195), Point(165,195))
Line2.draw(win)

Hand = Oval(Point(260,213), Point(265,220))
Hand.setFill("White")
Hand.draw(win)

Sun1part = Polygon(Point(30,30), Point(80,30), Point(55,80))
Sun1part.setFill("Yellow")

Sun2part = Polygon(Point(55,17), Point(30,67.26), Point(80, 67.26))
Sun2part.setFill("Yellow")

Sun1part.setOutline("Yellow")
Sun2part.setOutline("Yellow")

Sun1part.draw(win)
Sun2part.draw(win)

Smoke1 = Oval(Point(130,80), Point(160,60))
Smoke1.setFill("Grey")
Smoke1.draw(win)

Smoke2 = Oval(Point(140,70), Point(165,55))
Smoke2.setFill("White")
Smoke2.draw(win)

PondSide = Oval(Point(142.9,285.7), Point(367.5,367.5))
PondSide.setFill("Yellow")
PondSide.draw(win)

Pond = Oval(Point(150,300), Point(350,350))
Pond.setFill("Blue")
Pond.draw(win)

win.getMouse()
win.close()
