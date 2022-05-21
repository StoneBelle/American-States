from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-350, -280)
        self.valid_answers =\
            []
        self.score = 0


    def show_score(self, answer):
        self.clear()
        self.valid_answers.append(answer)
        self.score = len(self.valid_answers)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
