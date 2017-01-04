# Course: IT1 1120
# Assignment #1
# Tsang, Tyler
# 8659481


import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

#Draw first circle
t.circle(100)

#move to 2nd circle
t.penup()
t.goto(0,30)
t.pendown()

#draw second circle
t.circle(70)

#move to 3rd circle
t.penup()
t.goto(0,50)
t.pendown()

#draw third circle
t.circle(50)

#move to 4th circle
t.penup()
t.goto(0,80)
t.pendown()

#draw fourth circle
t.circle(20)

#move pen and draw
t.penup()
t.goto(0,-30)
t.pendown()
t.setheading(90)
t.forward(260)

#draw 2nd line
t.left(180)
t.forward(130)
t.left(45)
t.forward(130)
t.left(180)
t.forward(260)


#draw 3rd line
t.left(180)
t.forward(130)
t.left(45)
t.forward(130)
t.left(180)
t.forward(260)



#draw 4th line
t.left(180)
t.forward(130)
t.left(45)
t.forward(130)
t.left(180)
t.forward(260)

