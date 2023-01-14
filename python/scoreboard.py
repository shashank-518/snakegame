from turtle import Turtle
ALIGNMENT = "center"
X = 0
Y = 270

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(X, Y)
        self.update_score()
        self.hideturtle()


    def update_score(self):
         self.write(f"Score: {self.score}",align="center", font =("courier",24,"normal"))
       

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        
        # self.clear()
         self.goto(0, 0)
         self.write("GAME OVER", align="center", font =("courier",24,"normal"))
         self.color("White")
        
