"""
David Cooper
2104283
COSC 1336
Turtle Extra Credit
This whole drawing was made using only straight lines.
"""

import turtle

import math


GRID_SIZE = 750 #how big do you want the box?

num_lines = int(input("Please enter the number of lines you'd like to use, I recommend 15 to no more than 30:"))

dist_lines = GRID_SIZE / num_lines

dist_lines_mid = GRID_SIZE/4 / num_lines

d_lines_angled = GRID_SIZE/2 / num_lines

angle = math.sin(math.pi/4)

scn = turtle.Screen()
scn.bgcolor('Black')



bob = turtle.Turtle()
bob.speed(10)
bob.pu()
bob.forward(GRID_SIZE/2)
bob.right(90)
bob.forward(GRID_SIZE/2)
bob.pd()
bob.hideturtle()

#bob.pensize(5)
#the box
for i in range(2):
    bob.pencolor('White')
    bob.right(90)
    bob.forward(GRID_SIZE)

for i in range(2):
    bob.pencolor('Red')
    bob.right(90)
    bob.forward(GRID_SIZE)
    
#bob.pensize(1)

#the lines
for i in range(0, num_lines):
    bob.pencolor('White')
    bob.pu()
    bob.goto(-GRID_SIZE/2, GRID_SIZE/2 - dist_lines * i)
    bob.pd()
    bob.goto(-GRID_SIZE/2 + dist_lines * (1+i),-GRID_SIZE/2)
    bob.pu()


#floating diamond base
bob.home()

bob.pencolor('White')
bob.pd()
bob.forward(GRID_SIZE/4)
bob.forward(-GRID_SIZE/2)
bob.forward(GRID_SIZE/4)
bob.right(90)
bob.forward(GRID_SIZE/4)
bob.forward(-GRID_SIZE/2)
bob.pu()
bob.home()


#bob.pencolor('White')
#positive x poitive y side
for i in range(0, num_lines):
    #bob.pencolor('Red')
    bob.goto(0, GRID_SIZE/4 - dist_lines_mid * i)
    bob.pd()
    bob.goto(0 + dist_lines_mid * (1+i), 0)
    bob.pu()
   

#negative x positive y side
for i in range(0, num_lines):
    #bob.pencolor('Red')
    bob.goto(0, GRID_SIZE/4 - dist_lines_mid * i)
    bob.pd()
    bob.goto(0 - dist_lines_mid * (1+i), 0)
    bob.pu()
    
#negative x negative y side
for i in range(0, num_lines):
    #bob.pencolor('Red')
    bob.goto(0, -GRID_SIZE/4 + dist_lines_mid * i)
    bob.pd()
    bob.goto(0 - dist_lines_mid * (1+i), 0)
    bob.pu()
    
#positive x negative y side
for i in range(0, num_lines):
    #bob.pencolor('Red')
    bob.goto(0, -GRID_SIZE/4 + dist_lines_mid * i)
    bob.pd()
    bob.goto(0 + dist_lines_mid * (i+1), 0)
    bob.pu()

    
bob.home()

#top right corner of big grid
for i in range(0, num_lines):
    bob.pencolor('Red')
    bob.goto(-GRID_SIZE/2 + dist_lines * i, GRID_SIZE/2)
    bob.pd()
    bob.goto(GRID_SIZE/2, GRID_SIZE/2 - dist_lines * (1+i))
    bob.pu()


#drawing a bigger floating diamond
bob.home()

bob.pencolor('Red')
bob.right(45)
bob.pd()
bob.forward(GRID_SIZE/2)
bob.forward(-GRID_SIZE)
bob.forward(GRID_SIZE/2)
bob.right(90)
bob.forward(GRID_SIZE/4)
bob.forward(-GRID_SIZE/2)
bob.pu()
bob.home()

#upper left big diamond lines
for i in range(0, num_lines):
    bob.goto(((-GRID_SIZE/2 + d_lines_angled * i) * angle), (GRID_SIZE/2 - d_lines_angled * i) * angle)
    bob.pd()
    bob.goto((dist_lines_mid * angle) * (i + 1), (dist_lines_mid * angle) * (1 + i))
    bob.pu()

#upper right big diamond lines
for i in range(0, num_lines):
    bob.goto((dist_lines_mid * angle) * (i + 1), (dist_lines_mid * angle) * (1 + i))
    bob.pd()
    bob.goto(((GRID_SIZE/2 - d_lines_angled * i) * angle), (-GRID_SIZE/2 + d_lines_angled * i) * angle)
    bob.pu()

#lower right big diamond lines
for i in range(0, num_lines):
    bob.goto((-dist_lines_mid * angle) * (i + 1), (-dist_lines_mid * angle) * (1 + i))
    bob.pd()
    bob.goto(((GRID_SIZE/2 - d_lines_angled * i) * angle), (-GRID_SIZE/2 + d_lines_angled * i) * angle)
    bob.pu()

#lower left big diamond lines
for i in range(0, num_lines):
    bob.goto((-dist_lines_mid * angle) * (i + 1), (-dist_lines_mid * angle) * (1 + i))
    bob.pd()
    bob.goto(((-GRID_SIZE/2 + d_lines_angled * i) * angle), (GRID_SIZE/2 - d_lines_angled * i) * angle)
    bob.pu()



scn.exitonclick()
