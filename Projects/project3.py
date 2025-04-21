import turtle

t = turtle.Turtle()
#make color orange
t.goto(100, 0)
t.color("orange")
t.speed(10)
for i in range (53):
    t.forward(100)
    t.left(61)
t.pendown()
#move shape to another place than start drawing again
t.penup()
t.color("pink")
t.goto(-200, 190)
t.pendown()
t.speed(10)
for i in range (60):
    t.forward(100)
    t.right(61)
#use a different cord and make another shape
t.penup()
t.goto(0, -100)
t.color("purple")
t.pendown()
for i in range (10):
    t.forward (91)
    t.left (91)
    t.forward (91)
    t.left (91)
#repeat shape size but change letter
t.penup()
t.goto(-150, 145)
t.color ("red")
t.pendown()
t.speed(10)
for i in range (360):
    t.forward (1)
    t.right (1)

t.penup()
t.goto(150,135)
t.color("blue")
t.pendown()

for i in range (360):
    t.forward (1)
    t.right (1)
turtle.exitonclick()