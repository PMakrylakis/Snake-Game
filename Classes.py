from turtle import Turtle
import random as rnd

DIM = 600
STEP = 20

class Snake:
    def __init__(self):
        self.head=Turtle(shape='square')
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            body = Turtle(shape='square')
            body.penup()
            body.fillcolor("white")
            body.pencolor("grey")
            body.goto(x=-20 * i, y=0)
            body.setheading(0)
            body.speed("fast")
            self.segments.append(body)
        self.head=self.segments[0]

    def move(self):
        i = len(self.segments) - 1
        while i > 0:
            self.segments[i].speed('fast')
            self.segments[i].goto(x=self.segments[i - 1].xcor(), y=self.segments[i - 1].ycor())
            i -= 1
        self.head.forward(STEP)

    def face_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def face_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def face_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def face_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def check_for_boundaries(self):
        x,y= self.head.xcor(), self.head.ycor()
        if x >= DIM/2 or x <= -DIM/2:
            self.head.goto(x=-x, y=y)
        elif y >= DIM/2 or y <= -DIM/2:
            self.head.goto(x=x, y=-y)
        else:
            pass

    def target_hit(self,target):
        if abs(self.head.distance(target)) < 15:
            return True
        else:
            return False

    def crash(self):
        x_head, y_head = self.head.xcor(), self.head.ycor()
        for item in self.segments[2:]:
            x, y = item.xcor(), item.ycor()
            dif=((x-x_head)**2+(y-y_head)**2)**0.5
            #if x != x_head or y != y_head:
            #print(self.head.distance(item))
            if len(self.segments) < 5:
                continue
            elif abs(self.head.distance(item)) >= 20:
                continue
            else:
                return True
        return False

    def append_snake(self):
        new_body = Turtle(shape='square')
        new_body.penup()
        new_body.fillcolor("white")
        new_body.pencolor("grey")

        new_body.goto(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())
        new_body.setheading(self.segments[-1].heading())
        new_body.backward(STEP)
        self.segments.append(new_body)



class ScoringBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.game_is_on=True
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=DIM / 2 - 30)
        self.read_topScore()
        self.update_board()

    def read_topScore(self):
        filename = 'Top_Score.txt'
        try:
            with open(filename, 'r') as f:
                self.top_score=int(f.read())
        except FileNotFoundError:
            self.top_score =0

    def update_board(self):
        self.clear()
        self.write(f"Score= {self.score}, Top score= {self.top_score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.update_board()

    def update_top_score(self):
        filename = 'Top_Score.txt'
        if self.score > self.top_score:
            self.top_score = self.score
            try:
                with open(filename, 'w') as fil:
                    fil.write(f"{self.top_score}")
            except FileNotFoundError:
                print("File not found")

    def game_over(self):
        self.update_top_score()
        self.goto(x=0, y=DIM/4)
        self.write("GAME OVER!", move=False, align='center', font=('Arial', 32, 'bold'))
        self.game_is_on=False

class Target(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("red")
        self.shape('circle')
        self.fillcolor("red")
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.randomly_relocate()

    def randomly_relocate(self):
        self.goto(x=rnd.randint(-220, 220), y=rnd.randint(-220, 220))

