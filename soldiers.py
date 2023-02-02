import random
import turtle


# random function


def impact(bullet, sold):
    if bullet.pos() == sold.pos():
        sold.left(1440)


# Simulation loop
def sim_loop(red, blue):
    for r in red:
        if 20 < r.heading() < 340:
            r.seth(random.randrange(0, 25))
        r.left(random.randrange(-25, 25))
    for b in blue:
        b.seth(random.randrange(155, 205))


# Initial Spawn

red_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
blue_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
f_bullet_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]

# Red spawn
#                           vvvv - This is for IDE, keeps saying something is an error when it isn't (probably)
for r in red_list:  # noinspection PyRedeclaration
    r.color("red")
    r.penup()
    r.goto(random.randrange(-300, -158), random.randrange(-110, 110))
# Blue spawn
for b in blue_list:  # noinspection PyRedeclaration
    b.color("blue")
    b.penup()
    b.goto(random.randrange(158, 300), random.randrange(-110, 110))
for b in blue_list:
    b.seth(180)

sim_loop(red_list, blue_list)
screen = turtle.Screen()

turtle.done()
