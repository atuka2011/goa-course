
from turtle import *
#we start drawing a home
#we start drawing a square

speed(5)
width(6)
 
color("brown")

begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()

#end of square       

#drawing a door


forward(50)
color("green")
begin_fill()
left(90)
forward(70) #height of a door
right(90)   
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(150,150)
pendown()

color("blue")
begin_fill()
right(150)
forward(150)
left(120)
forward(150)
end_fill()



penup()
goto(100,100)
pendown()



left(120)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)

penup()
goto(50,100)
pendown()

left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)

exitonclick()





















































