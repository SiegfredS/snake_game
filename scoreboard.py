from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
GAME_OVER_FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self,
                 score=0):
        super().__init__()
        self.score = score
        with open(file="score_data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.show()

    def show(self):
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        else:
            pass
        self.write(f"Score {self.score}, High Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT,)

    def reset_scoreboard(self):
        if self.score >= self.high_score:
            with open("score_data.txt", mode="w") as data:
                data.write(f"{self.score}")
        else:
            pass
        self.score = 0
        self.update()
