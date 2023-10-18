#六边形
import turtle
from turtle import *

setup(1280,720,0,0)
pen(pencolor="orange", fillcolor="orange", pensize=10)
penup()
fd(-500)
pendown()
right(60)
begin_fill()
for i  in range(6):
    fd(100)
    right(-60)
end_fill()
hideturtle()
done()

