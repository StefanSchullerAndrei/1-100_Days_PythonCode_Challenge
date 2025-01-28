from turtle import Turtle
from types import new_class

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Challenge: Create 3 turtles and position them next to each other.
    # Each turtle should be a white square (default size: 20x20)


    def create_snake(self):
        # ---------------- Method 1 -----------------------
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
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

# Programming the snake to automatically move forward and figuring out a way for the tail of the snake to follow where the head is going
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):   # start = is the number that we're going to start the range from,
                new_x = self.segments[seg_num - 1].xcor()        # stop = is where the range is going to end
                new_y = self.segments[seg_num - 1].ycor()            # step = is how we're going to get from the start to the stop
                self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)