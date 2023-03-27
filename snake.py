from turtle import Turtle


SNAKE_GREEN = "#006400"
MOVE_UNIT = 20

starting_coordinates = [(-40, 0), (-20, 0), (0, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in starting_coordinates:
            new_segment = Turtle("square")
            new_segment.color(SNAKE_GREEN)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[seg_num - 1].xcor()
            new_y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cor, new_y_cor)
        self.snake_head.forward(MOVE_UNIT)

    def up(self):
        self.snake_head.setheading(90)

    def down(self):
        self.snake_head.setheading(270)

    def left(self):
        self.snake_head.setheading(180)

    def right(self):
        self.snake_head.setheading(0)





