from setup import MyScreen
from Snake import Snake


screen = MyScreen()
screen.screen_setup()
snake_params = screen.get_snake_parameters()
snake = Snake(params=snake_params)

screen.screen.exitonclick()