import random
import turtle
import asyncio


def wiggle(red, blue):
    r_turtle = random.choice(red)
    if 20 < r_turtle.heading() < 340:
        r_turtle.seth(random.randrange(0, 25))
    r_turtle.left(random.randrange(-25, 25))
    b_turtle = random.choice(blue)
    b_turtle.seth(random.randrange(155, 205))


async def bullet(launcher):
    bul = launcher.clone()
    bul.color("black")
    bul.seth(launcher.heading())
    travel = 0
    while travel < 700:
        bul.forward(5)
        travel += 5
    bul.hideturtle()


# Simulation loop

async def sim_loop(red, blue):
    wiggle(red, blue)
    if random.randrange(0, 50) <= 5:
        asyncio.run(bullet(random.choice(red)))


# Initial Spawn

red_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
blue_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
r_count = 0
b_count = 0
# Red spawn
for r in red_list:  # noinspection PyRedeclaration
    r_count += 1
    r.color("red")
    r.penup()
    r.goto(random.randrange(-300, -158), random.randrange(-110, 110))
# Blue spawn
for b in blue_list:  # noinspection PyRedeclaration
    b_count += 1
    b.color("blue")
    b.penup()
    b.goto(random.randrange(158, 300), random.randrange(-110, 110))
    b.seth(180)

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
while r_count > 0 and b_count > 0:
    asyncio.run(sim_loop(red_list, blue_list))
screen = turtle.Screen()
loop.close()
turtle.done()
