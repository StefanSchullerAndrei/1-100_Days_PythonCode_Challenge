# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
#
# for _ in range(100):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
import random
import turtle
import turtle as t # creating new object with an allias name
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b) # how to return a tuple with the random colours)
    return color
# colours = ["medium spring green", "medium blue", "dark orange", "yellow"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

# for _ in range(200):
#     tim.color(olor())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()
