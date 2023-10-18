from turtle import Screen
from Classes import *   # These are the classes I defined
import time

play= "yes"
while play[0] != 'n':

    # Initialize the Screen object
    screen = Screen()
    screen.reset()
    screen.setup(height=DIM, width=DIM)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    # Initialize Snake, Target, Scoring Board
    snake = Snake()
    target = Target()
    board = ScoringBoard()

    # Define keys for snake control and enable screen to listen
    screen.onkey(snake.face_east, 'd')
    screen.onkey(snake.face_west, 'a')
    screen.onkey(snake.face_north, 'w')
    screen.onkey(snake.face_south, 's')
    screen.onkey(screen.clear, 'c')
    #screen.onkeypress(snake.append_snake, 'v')
    screen.listen()

    while board.game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()                        # Snake is moving
        snake.check_for_boundaries()        # It reappears on the opposite side

        if snake.target_hit(target):        # Snake catches target
            board.update_score()            # Update the board
            snake.append_snake()            # Increase snake size
            target.randomly_relocate()      # Randomly relocate the target

        if snake.crash():                   # Snake crashes on itself
            board.game_over()               # Stop Game
            print("You crashed, game over...")
            time.sleep(0.2)

    print(f"Your score is: {board.score}\n")
    if board.score>=board.top_score:
        print("Bravo, a new top score!")

    # Ask if user wants to play again
    play=screen.textinput(title="SnakeGame Input Prompt", prompt="Do you want to play again? [y/n]").lower()
    if play== 'n':
        screen.reset()
        screen.exitonclick()

print("Goodbye...")
