from time import sleep


def game_over(snake, food_pellet, big_food, screen, score_board):
    """Activates the game over sequence."""
    score_board.game_over(snake, food_pellet, big_food)
    screen.update()
    sleep(1)
    # score_board.clear()
    snake.reset()
    score_board.reset(food_pellet, big_food)

    return True


def check_game_over(snake, food_pellet, big_food, screen, score_board):
    """Checks to see if the snake has activated any of the conditions that
    cause the game to be over."""
    # Detects collission with wall
    # if (snake.head.xcor() <= -295 or snake.head.xcor() >= 295 or
    #         snake.head.ycor() <= -295 or snake.head.ycor() >= 295):
    #     return game_over(snake, food_pellet, big_food, screen, score_board)

    # detects collission with its own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            return game_over(snake, food_pellet, big_food, screen, score_board)

    # returns a true value if none of the game over conditions are satisfied
    return False
