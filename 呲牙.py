from turtle import * 

def mouth():  
    pencolor("darkred")
    pensize(6)
    fillcolor("white") 
    begin_fill()
    for i in range(180): 
        right(1)
        fd(1.7)
    right(90)  
    fd(195)
    end_fill()

def eye(): 
    pensize(10)
    pencolor("darkred")
    for i in range(180):  
        right(1)
        fd(0.4)

def pos(x, y):  
    penup()
    goto(x, y)
    pendown()

def teech(l, x):  
    pensize(5)
    pencolor("goldenrod")
    pos(x, 120)
    fd(l)

def brow():
    pencolor("darkred")
    pensize(8)
    for i in range(160):
        right(1)
        fd(0.6)

speed(9)
delay(0)
pensize(3)
pencolor("peru")
fillcolor("gold")
begin_fill()
circle(120) 
end_fill()
right(90)
pos(100, 120)  
mouth()  
pos(30, 170)  
left(90)
eye()
pos(-75, 170) 
right(180)
eye()
teech(89, 20)
teech(70, 60)
teech(88, -20)
teech(68, -60)
pos(-95, 120)
pencolor("darkred")
pensize(5)
left(90)
fd(195)
pos(30, 220)
left(80)
brow()
pos(-90, 220)
right(200)
brow()
hideturtle()  
done() 