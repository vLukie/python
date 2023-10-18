from turtle import *

def eye(col, rad):
     down()
     fillcolor(col)
     begin_fill()
     circle(rad)
     end_fill()
     up()

speed(9)
delay(0)
pensize(3)
pencolor("peru")
fillcolor("gold")
begin_fill()
circle(100)
end_fill()
up()
 
pencolor("black")
goto(-40, 120)
eye('white', 18)
goto(-37, 125)
eye('black', 8)
goto(40, 120)
eye('white', 18)
goto(40, 125)
eye('black', 8)
 
pencolor("darkred")
pensize(5)
goto(-40, 85)
down()
right(90)
circle(40, 180)
up()

hideturtle()
done()

