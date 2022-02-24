from turtle import Turtle
import random


class Food(Turtle):
    """Creates a 'Food' class."""

    def __init__(self):
        """Initializes the attributes of the food class and inherits from
        the turtle class."""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.goto_random_location()

    def goto_random_location(self):
        """Creates a food pellet at a random location on the screen."""
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)


class BigFood(Food):
    """Creates a BigFood class i.e. a bigger food that gives more points"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        # self.shapesize(stretch_len=2, stretch_wid=2)
        self.color('red')

    def goto_random_location(self):
        super().goto_random_location()
        self.showturtle()
