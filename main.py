from turtle import Screen
from snake import Snake
import time
from food import Food

SCREEN_GRAY = "#708090"
SNAKE_GREEN = "#006400"

starting_coordinates = [(-40, 0), (-20, 0), (0, 0)]

screen = Screen()
screen.setup(600, 600)
screen.bgcolor(SCREEN_GRAY)
screen.title("Get A Grip On My Snake")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

my_snake_is_long = True
while my_snake_is_long:
    screen.update()
    time.sleep(0.2)
    snake.move()


screen.exitonclick()

# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
