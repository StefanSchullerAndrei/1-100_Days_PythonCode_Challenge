from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)   # setting the window size
screen.bgcolor("black") # changing the background of the console
screen.title("My Snake Game")
screen.tracer(0)

# Challenge: Create 3 turtles and position them next to each other.
#Each turtle should be a white square (default size: 20x20)

# ---------------- Method 1 -----------------------

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

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



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):   # start = is the number that we're going to start the range from,
            new_x = segments[seg_num - 1].xcor()        # stop = is where the range is going to end
            new_y = segments[seg_num - 1].ycor()            # step = is how we're going to get from the start to the stop
            segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)



screen.exitonclick()
