import random
import turtle
import asyncio


async def movement(red, blue):
    r_turtle = random.choice(red)
    if 20 < r_turtle.heading() < 340:
        r_turtle.seth(random.randrange(0, 25))
    r_turtle.left(random.randrange(-25, 25))
    b_turtle = random.choice(blue)
    b_turtle.seth(random.randrange(155, 205))


async def bullet(shooter):
    print("Confirmed")
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

async def main(red, blue):
    await asyncio.gather(bullet(random.choice(red)), bullet(random.choice(blue)), movement(red, blue))


# Initial Spawn
red_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
            turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
blue_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
             turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
r_count = 0
b_count = 0
# Red spawn
for r in red_list:  # noinspection PyRedeclaration
    r_count += 1
    r.color("red")
    r.penup()
    r.goto(random.randrange(-350, -125), random.randrange(-200, 200))
# Blue spawn
for b in blue_list:  # noinspection PyRedeclaration
    b_count += 1
    b.color("blue")
    b.penup()
    b.goto(random.randrange(125, 350), random.randrange(-200, 200))
    b.seth(180)

# Main loop
while r_count > 0 and b_count > 0:
    asyncio.run(main(red_list, blue_list))

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
screen = turtle.Screen()
loop.close()
turtle.done()
