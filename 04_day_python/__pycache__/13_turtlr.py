import turtle as t 
import random
spring=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
spring.speed('fastest')
def draw_sprigograpgh(size_of_gap):
    for _ in range(int(360/size_of_gap)):
       spring.color(random_color())
       spring.circle(100) 
       spring.setheading(spring.heading()+size_of_gap)
draw_sprigograpgh(5)
screen=t.Screen()
screen.exitonclick()