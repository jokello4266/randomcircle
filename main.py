import turtle
from turtle import Turtle, Screen
import random


tim = turtle.Turtle()
turtle.colormode(255)

# colors = ["burlywood","forest green","light salmon","slate blue","orange red"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


"""
directions = [0, 90, 180,270 ]
tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    #tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
"""

# changing my tuple to a list
"""my_tuple = (1,2.3)
    list(my_tuple)
"""

# Udemy day 18 - exercise 172 - Creating Spirograph

tim.speed("fastest")
"""
for _ in range(100):
    tim.circle(100)
    tim.color(random_color())
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

# tim.circle(100)
 current_heading = tim.heading()
    tim.setheading(current_heading + 10) 
    OR
    tim.setheading(tim.heading() + 10)

"""

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)






screen = Screen()
screen.exitonclick()