from turtle import Screen


class MyScreen:
    def __init__(self):
        # Bug: can't do MyScreen(Screen) then super().__init__
        self.screen = Screen()


    def screen_setup(self,
                     bgcolor="black",
                     width=600,
                     height=600,
                     title="Snake Game"):
        self.screen.setup(width=width, height=height)
        self.screen.title(titlestring=title)
        self.screen.bgcolor(bgcolor)
        self.screen.tracer(0)

    def get_snake_parameters(self):
        color = self.screen.textinput("Color of Snake", "Input color of snake:")
        length = self.screen.numinput("Snake Length", "Input initial length of snake:")
        return (color, int(length))
