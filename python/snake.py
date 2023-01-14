from turtle import Turtle,Screen
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_FORWARD = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake:
    def __init__(self):
        self.segement = []
        self.create_snake()
        self.head = self.segement[0]

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)

    def add_segment(self,position):
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(position)
            self.segement.append(new)

    def create_segment(self):
        self.add_segment(self.segement[-1].position())

    def move(self):
            for seg in range(len(self.segement)-1,0,-1):
                new_x =self.segement[seg -1].xcor()
                new_y =self.segement[seg -1 ].ycor()
                self.segement[seg].goto(new_x,new_y)
            self.head.forward(MOVE_FORWARD)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # def new_box(self):
    #     for
    #     new = Turtle("Square")