import random
import turtle
import asyncio
import threading


def movement(red, blue):
    r_turtle = random.choice(red)
    if 20 < r_turtle.heading() < 340:
        r_turtle.seth(random.randrange(0, 25))
    r_turtle.left(random.randrange(-25, 25))
    b_turtle = random.choice(blue)
    b_turtle.seth(random.randrange(155, 205))


def bullet(shooter):
    if random.randrange(0, 50) <= 5:
        bul = shooter.clone()
        bul.color("black")
        bul.seth(shooter.heading())
        travel = 0
        while travel < 700:
            bul.forward(5)
            bul.pos()
            travel += 5
        bul.hideturtle()
        bul.clear()
        del bul
    else:
        pass


# Simulation loop

# def main(red, blue):
#    pass


# Initial Spawn
def spawn(amt):
    spawn.red_list = []
    spawn.blue_list = []
    for _ in range(amt):
        spawn.red_list.append(turtle.Turtle())
        spawn.blue_list.append(turtle.Turtle())
    spawn.r_count = 0
    spawn.b_count = 0
    # Red spawn
    for r in spawn.red_list:  # noinspection PyRedeclaration
        spawn.r_count += 1
        r.color("red")
        r.penup()
        r.goto(random.randrange(-350, -125), random.randrange(-200, 200))
    # Blue spawn
    for b in spawn.blue_list:  # noinspection PyRedeclaration
        spawn.b_count += 1
        b.color("blue")
        b.penup()
        b.goto(random.randrange(125, 350), random.randrange(-200, 200))
        b.seth(180)




# Main loop
spawn(4)
# noinspection PyUnresolvedReferences
while spawn.r_count > 0 and spawn.b_count > 0:  # noinspection PyUnresolvedReferences
    movement(spawn.red_list, spawn.blue_list)


screen = turtle.Screen()
turtle.done()
