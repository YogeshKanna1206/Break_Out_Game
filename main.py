import turtle
import time
import random

wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-270,260)
score_display.write(f"Score: {score}",font=("Arial",16,"bold"))

lives =3
lives_display = turtle.Turtle()
lives_display.color("white")
lives_display.penup()
lives_display.hideturtle()
lives_display.goto(200,260)
lives_display.write(f"Lives: {lives}", font=("Arial", 16, "bold"))



paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("orange")
paddle.shapesize(stretch_wid=1,stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

def move_left():
    x = paddle.xcor()
    if x>-260:
        paddle.setx(x-20)
def move_right():
    x = paddle.xcor()
    if x<260:
        paddle.setx(x+20)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = -3

bricks = []
colors = ["blue","red","yellow","green","blue"]
y_start = 250
for row in range(5):
    for col in range(-5, 6):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.shapesize(stretch_wid=1,stretch_len=3)
        brick.penup()
        brick.goto(col*55,250-row*30)
        bricks.append(brick)


bricks_remaining = len(bricks)
while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.xcor()>290 or ball.xcor()<-290:
        ball.dx *= -1

    if ball.ycor()>290:
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.goto(0,0)
        lives -=1
        lives_display.clear()
        lives_display.write(f"Lives: {lives}", font=("Arial", 16, "bold"))
        ball.dy *= -1
        if lives == 0:
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            break
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1
    for brick in bricks:
        if brick.distance(ball) < 30:
            score+=1
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1
            bricks_remaining -= 1
            score_display.clear()
            score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))
            if bricks_remaining == 0:
                score_display.goto(0, 0)
                score_display.write("YOU WIN!", align="center", font=("Arial", 24, "bold"))
                break
            break

    time.sleep(0.001)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")


while True:
    wn.update()