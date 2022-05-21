from turtle import Turtle


class Answers(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def show_state(self, x_pos, y_pos, state):
        """Writes the state name on its appropriate position on map."""
        self.setpos(x_pos, y_pos)
        self.write(state, align="center", font=("Arial", 8, "normal"))
