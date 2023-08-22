from setup import MyScreen
from Snake import Snake


screen = MyScreen()
screen.screen_setup()
snake_params = screen.get_snake_parameters()
snake = Snake(params=snake_params)

# After all initial setup, update screen
screen.screen.update()

screen.screen.exitonclick()
