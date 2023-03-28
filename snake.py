from turtle import Turtle


SNAKE_GREEN = "#006400"
MOVE_UNIT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_coordinates = [(-40, 0), (-20, 0), (0, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in starting_coordinates:
            self.grow_snake(position)

    def grow_snake(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def elongate_snake(self):
        self.grow_snake(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[seg_num - 1].xcor()
            new_y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cor, new_y_cor)
        self.snake_head.forward(MOVE_UNIT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)





