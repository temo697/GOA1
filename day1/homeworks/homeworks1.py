from turtle import *

#we want to paint a house

#step 1: draw a square
width(3)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("purple")
left(90)

forward(120)
right(90)

forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)

forward(200)
left(120)

forward(200)
end_fill()

color("green")

left(30)
forward(50)

left(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

penup()
goto(200,200)
pendown()

left(90)
forward(50)

right(90)
forward(40)

left(90)
forward(35)

left(90)
forward(40)






exitonclick()