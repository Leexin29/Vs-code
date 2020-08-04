# SevenDigitalsDrawV2.py
import turtle
import datetime
import time


def drawGap():  # 绘制数码管间隔
    turtle.pu()
    turtle.fd(5)


def drawLine(draw):  # 绘制单个数码管
    drawGap()
    if draw:
        turtle.pd()
    else:
        turtle.pu()

    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigital(d):  # 根据数字绘制7段数码管
    if d in [2, 3, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)
    if d in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)
    if d in [0, 2, 3, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)
    if d in [0, 2, 6, 8]:
        drawLine(True)
    else:
        drawLine(False)
    turtle.left(90)
    if d in [0, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)
    if d in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)
    if d in [0, 1, 2, 3, 4, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)
    turtle.left(180)
    turtle.pu()
    turtle.fd(20)


def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '年':
            turtle.write('年', font=("等线", 26, "normal"))
            turtle.pencolor("green")
            turtle.fd(60)
        elif i == '月':
            turtle.write('月', font=("等线", 26, "normal"))
            turtle.pencolor("blue")
            turtle.fd(60)
        elif i == '日':
            turtle.write('日', font=("等线", 26, "normal"))
            turtle.pencolor("red")
            turtle.goto(-210, -50)
        elif i == '时':
            turtle.write('时', font=("等线", 26, "normal"))
            turtle.pencolor("green")
            turtle.fd(60)
        elif i == '分':
            turtle.write('分', font=("等线", 26, "normal"))
            turtle.pencolor("blue")
            turtle.fd(60)
        elif i == '秒':
            turtle.write('秒', font=("等线", 26, "normal"))
        else:
            drawDigital(eval(i))


def main():
    turtle.setup(900, 500)
    while True:
        turtle.tracer(False)  # 关闭turtle
        turtle.reset()  # 重置turtle
        turtle.pu()
        turtle.goto(-350, 100)
        turtle.pensize(5)
        drawDate(datetime.datetime.now().strftime(
            '%Y年%m月%d日%H时%M分%S秒'))  # 获取系统时间
        time.sleep(1)  # 刷新
        turtle.hideturtle()
    turtle.done()


main()
