import turtle as turtle_module
import random
turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
color_list  = [(25,25,112),(47,79,79),(0,0,0),(54,69,79),(72,61,139),(85,107,47),(139,0,0),(0,100,0),(0,0,139),(105,105,105),
               (25,25,25),(60,20,20),(70,70,70),(36,36,62),(64,0,64),(34,139,34),(85,26,139),(112,128,144),(90,0,90),(0,0,70)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count  in range(1, number_of_dots):
    tim.dot(20,random.choice(color_list))
    tim .forward(50)
    if dot_count % 10 ==0:
       tim.setheading(90)
       tim.forward(50)
       tim.setheading(180)
       tim.forward(500)
       tim.setheading(0)   