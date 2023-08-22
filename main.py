from setup import MyScreen
from Snake import Snake
import time


screen = MyScreen()
screen.screen_setup()
snake_params = screen.get_snake_parameters()
my_screen = screen.screen
snake = Snake(params=snake_params)
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

my_screen.exitonclick()
