# ####################################
# ### SETUP ###
import turtle
# ###################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("yellow")
t.pendown()

for i in range(10):
    for i in range(4):
        t.forward(10)
        t.left(90)
    t.penup()
    t.forward(30)
    t.pendown()

    

#
# ### ENDING ###
turtle.exitonclick()
# ###########################   