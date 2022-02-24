from turtle import Turtle


FONT = ("Courier", 14, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    """Creates a scoreboard class."""

    def __init__(self):
        """Initializes the attributes of the scoreboard and inherits from the
        Turtle class."""
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.display_score()

    def increase_score(self, double=False):
        if double == False:
            self.score += 1
        elif double == True:
            self.score += 2
        if self.score > self.high_score:
            self.high_score = self.score
        self.display_score()

    def display_score(self):
        self.goto(0, 270)
        self.clear()
        self.text = f"Score: {self.score} | High score: {self.high_score}"
        self.write(arg=self.text, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self, snake, food, big_food):
        game_over_msg = f"Game Over! Your final score was {self.score}."
        # for i in range(len(snake.segments)):
        #     snake.segments[i].hideturtle()
        if len(big_food) != 0:
            big_food[0].hideturtle()
        food.hideturtle()
        self.penup()
        self.clear()
        self.home()
        self.write(arg=game_over_msg, move=False,
                   align=ALIGNMENT, font=FONT)
        with open("high_score.txt", mode='w') as file:
            file.write(str(self.high_score))

    def reset(self, food, big_food):
        self.score = 0
        self.display_score()
        food.showturtle()
        if len(big_food) != 0:
            big_food[0].showturtle()


"""
class FoodTimer(Turtle):
    Creates a food timer that tells how long there is till the red food
disappears.

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(150, 270)
        self.color('white')

    def display_time(self, remaining_time):
        Displays the time left till the red food disappears.
        time_left_msg = f"Red Pellet: {remaining_time}"
        self.clear()
        self.write(arg=time_left_msg, align=ALIGNMENT, font=FONT)
        if remaining_time == 1:
            self.clear()
"""
