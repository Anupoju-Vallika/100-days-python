from turtle import Turtle
import os

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        # Path to data.txt in the same folder as this file
        self.file_path = os.path.join(os.path.dirname(__file__), "data.txt")

        # Read the high score from the file
        with open(self.file_path) as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", 
                   align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.file_path, "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
