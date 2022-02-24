from turtle import Screen, Turtle
import time as t
from snake import Snake
from food import Food, BigFood
from scoreboard import ScoreBoard  # , FoodTimer
from game_over_functions import check_game_over
import random as r


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
player_name = screen.textinput("Player Name", "Enter your name: ").title()
screen.title(f"The Snake Game — Welcome, {player_name}")
screen.tracer(0)

snake = Snake()
food_pellet = Food()
score_board = ScoreBoard()
big_food = []
# red_food_timer = FoodTimer()

screen.update()
t.sleep(2)
game_active = True
speed = 0.05

# game_run_time is the same as the time at which the big food was created
game_run_time = int(t.time())
time_left = 0
new_round = False
while game_active:
    # the two lines below essentially refreshes the screen every .1 seconds
    screen.update()
    t.sleep(speed)

    # calls the function to move the snake
    snake.move()

    # Detect collision with food and do needed functions if so.
    if snake.head.distance(food_pellet) < 10:
        food_pellet.goto_random_location()
        score_board.increase_score()
        snake.add_segment()
        snake.move()

    # Create and detect collision with big food
    current_time = t.time()
    if current_time - game_run_time >= 10 and not big_food:
        big_food.append(BigFood())
        big_food[0].goto_random_location()
        time_left = 5
        game_run_time = int(t.time())
    if current_time - game_run_time >= 5 and len(big_food) != 0:
        big_food[0].hideturtle()
        big_food.clear()
        game_run_time = int(t.time())
    elif len(big_food) != 0:
        if snake.head.distance(big_food[0]) < 10:
            score_board.increase_score(double=True)
            big_food[0].hideturtle()
            big_food.clear()
            game_run_time = int(t.time())

    # Detect collision with wall.
    if (snake.head.xcor() <= -300 or snake.head.xcor() >= 300 or
            snake.head.ycor() <= -300 or snake.head.ycor() >= 300):
        snake.move_through_wall()

    # Detects collision with its own body
    new_round = check_game_over(
        snake, food_pellet, big_food, screen, score_board)


screen.exitonclick()
