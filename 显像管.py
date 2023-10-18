import turtle
import time

def drawGap(): 
    turtle.penup()
    turtle.fd(5)

def drawLine(draw): 
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90) 

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup() #为绘制后续数字确定位置
    turtle.fd(20)

def drawDate(date): #获得要输出的数字
    turtle.pencolor("PINK")
    for i in date:
        if i == '-':
            turtle.write("时",font=("Arial",18,"normal"))
            turtle.pencolor("BLUE")
            turtle.fd(40)
        elif i == '+':
            turtle.write("分",font=("Arial",18,"normal"))
            turtle.pencolor("GREEN")
            turtle.fd(40)
        elif i == '=':
            turtle.write("秒",font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i)) #通过eval()函数将数字变为整数

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    date = time.strftime("%H-%M+%S=",time.gmtime())
    print(date)
    drawDate(date)
    
    turtle.hideturtle()
    turtle.done()

main()

