#绘制七段数码管
from turtle import *
from datetime import datetime
from time import sleep
#tototo
def drawGap():
    up()
    fd(5)

def drawLine(draw):    
    drawGap()
    down() if draw else penup()    
    fd(40)    
    drawGap()    
    right(90)

def drawDigit(d):    
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)    
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)    
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)    
    drawLine(True) if d in [0,2,6,8] else drawLine(False)    
    left(90)    #第4段到第5段无需右转，相当于修正了方向    
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)    
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)    
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)    
    left(180)    
    up()    
    fd(20)
#绘制当前时间
def drawDate(date):    
    pencolor("red")    
    for i in date:        
        if i == '-':            
            write('年',font=('Arial',18,'normal'))            
            pencolor('orange')            
            fd(40)        
        elif i == '=':            
            write('月',font=('Arial',18,'normal'))            
            pencolor('yellow')            
            fd(40)        
        elif i == '+':            
            write('日',font=('Arial',18,'normal'))            
            pencolor('green')            
            fd(40)        
        elif i == '*':            
            write('时',font=('Arial',18,'normal'))            
            pencolor('blue')            
            fd(40)        
        elif i == '#':            
            write('分',font=('Arial',18,'normal'))            
            pencolor('purple')            
            fd(40)        
        elif i == '?':            
            write('秒',font=('Arial',18,'normal'))            
            fd(40)        
        else:            
            drawDigit(eval(i))
#主函数
def main():    
    setup(1300,280,50,300)    
    speed(0)    
    up()    
    fd(-600)    
    pensize(5)    
    while(1):        
        penup()        
        goto(-600,0)        
        pendown()        
        tracer(False)        
        pencolor('red')        
        drawDate(datetime.now().strftime('%Y-%m=%d+%H*%M#%S?'))    #获取当前系统时间         
        hideturtle()        
        sleep(1)        
        clear()  #清屏    
    done()
main()