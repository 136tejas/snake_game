from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

wn = Screen()
wn.setup(width=600, height=600)
wn.title("Snake Game")
wn.bgcolor("light blue")
wn.tracer(0)

snake = Snake()
food = Food()
score = Score()

wn.listen()
wn.onkey(snake.up, "w")
wn.onkey(snake.down, "s")
wn.onkey(snake.left, "a")
wn.onkey(snake.right, "d")

game_on = True
while game_on:
    wn.update()
    time.sleep(0.1)
    snake.move()

    # detect food and change the location.
    if snake.head.distance(food) < 17:
        snake.extend()
        food.refresh()
        score.incease_score()

    # detect wall and end game.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # detect tail and game over.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


wn.exitonclick()
