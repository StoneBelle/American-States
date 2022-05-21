from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-320, -280)
        self.valid_answers = []
        self.score = 0
        self.show_score()

    def update_score(self, answer):
        self.clear()
        self.valid_answers.append(answer)
        self.score = len(self.valid_answers)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
