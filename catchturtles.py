import turtle
import random


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("CatchTurtle 2")


scoree = 0
game_over = False
turtlelist = []

# SCORE TURTLE
score = turtle.Turtle()
score.color("red")
score.penup()
score.goto(0, 260)
score.hideturtle()
score.write("Score: 0", align="center", font=("Arial", 18, "bold"))

# COUNTDOWN TURTLE
countdown = turtle.Turtle()
countdown.color("white")
countdown.penup()
countdown.hideturtle()
countdown.goto(0, 220)


def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.color("yellow")
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x, y)
    t.hideturtle()
    turtlelist.append(t)
    t.onclick(handle_click)


def handle_click(x, y):
    global scoree, game_over
    if not game_over:
        scoree += 1
        score.clear()
        score.write(f"Score: {scoree}", align="center", font=("Arial", 18, "bold"))

x_cor = [-300, -150, 0, 150, 300]
y_cor = [-200, -100, 0, 100, 200]

def turtleposition():
    for x in x_cor:
        for y in y_cor:
            make_turtle(x, y)


def hide_turtles():
    for t in turtlelist:
        t.hideturtle()

def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtlelist).showturtle()
        screen.ontimer(show_turtle_randomly, 800)  # 0.8 saniyede bir değiştir


def count_down(time):
    global game_over
    countdown.clear()
    if time > 0:
        countdown.write(f"Time: {time}", align="center", font=("Arial", 18, "bold"))
        screen.ontimer(lambda: count_down(time - 1), 1000)
    else:
        countdown.clear()
        countdown.write("Time's up!", align="center", font=("Arial", 24, "bold"))
        hide_turtles()
        game_over = True


turtle.tracer(0)
turtleposition()
hide_turtles()
show_turtle_randomly()
count_down(60)  # 60 saniye
turtle.tracer(1)

turtle.mainloop()
