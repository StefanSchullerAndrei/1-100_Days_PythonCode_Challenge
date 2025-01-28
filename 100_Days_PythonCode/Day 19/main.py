from turtle import Turtle, Screen, clearscreen
import random
screen = Screen()

# def move_forward():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     # tim.clear()
#     # tim.home()
#     # tim.clear()    a method to reset to the center of the screen
#
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")

is_race_on = False
screen.setup(1000, 1000)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-490, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            print(turtle.color())


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()

