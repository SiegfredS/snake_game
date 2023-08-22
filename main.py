from setup import MyScreen
from snake import Snake
from food import Food
import time


screen = MyScreen()
screen.screen_setup()
snake_params = screen.get_snake_parameters()
my_screen = screen.screen
snake = Snake(params=snake_params)
food = Food()
# After all initial setup, update screen
my_screen.update()

# Functions on press
is_playing = True
my_screen.listen()
my_screen.onkeypress(fun=snake.snake_up, key="Up")
my_screen.onkeypress(fun=snake.snake_down, key="Down")
my_screen.onkeypress(fun=snake.snake_right, key="Right")
my_screen.onkeypress(fun=snake.snake_left, key="Left")

while is_playing:
    my_screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) <= 15:
        food.respawn()
        snake.add_segment()

    if snake.has_collided():
        is_playing = False
    else:
        pass

my_screen.exitonclick()
