from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)   # setting the window size
screen.bgcolor("black") # changing the background of the console
screen.title("My Snake Game")

# Challenge: Create 3 turtles and position them next to each other.
#Each turtle should be a white square (default size: 20x20)

# ---------------- Method 1 -----------------------

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

# ----------------- Method 2 ---------------------
# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(x= -20, y= 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(x=-40, y=0)


screen.exitonclick()