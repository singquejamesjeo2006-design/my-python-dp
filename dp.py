import turtle
import time
import random

score = 0
delay = 0.1

screen = turtle.Screen()
screen.title("Snake Eating Apple Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Apple
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 100)

# Snake body
body = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center",
          font=("Arial", 20, "bold"))

# Movement
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Main game loop
while True:
    screen.update()

    # Wall collision
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):

        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in body:
            segment.goto(1000, 1000)

        body.clear()
        score = 0
        pen.clear()
        pen.write("Score: 0", align="center",
                  font=("Arial", 20, "bold"))

    # Eat apple
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("green")
        segment.penup()
        body.append(segment)

        score += 10
        pen.clear()
        pen.write("Score: {}".format(score),
                  align="center",
                  font=("Arial", 20, "bold"))

    # Move body
    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in body:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for part in body:
                part.goto(1000, 1000)

            body.clear()
            score = 0
            pen.clear()
            pen.write("Score: 0", align="center",
                      font=("Arial", 20, "bold"))

    time.sleep(delay)
