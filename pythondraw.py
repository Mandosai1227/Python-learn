import turtle #程序关键  这里import是引入导入的意思，turtle是一个库
turtle.setup(650,350,200,200) #turtle.setup(width,height,startx,starty) 窗口的height和width、窗口离显示器边缘的距离，4个参数中后两个可选，setup()不是必须的
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()

#Python语法元素理解
#-Python蟒蛇绘制共17行代码，但是很多行类似
#-清楚理解这17行代码能够掌握Python基本绘图方法
#-参考框架结构，逐行分析，逐词理解

#程序参数的改变
#-Python蟒蛇的颜色：黑色，白色，七彩色...
#-Python蟒蛇的长度：1节，3节，10节...
#-Python蟒蛇的方向：向左走，斜着走...

#举一反三
#计算问题的扩展
#-Python蟒蛇绘制问题是各类图像绘制问题的代表
#-圆形绘制、五角星绘制、国旗绘制、机器猫绘制...
#-掌握绘制一条线的方法，就可以绘制整个世界
