import random
import turtle
import time
from threading import Thread


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
def main():
    movement(spawn.red_list, spawn.blue_list)
    if spawn.r_count != 0:
        bullet(random.choice(spawn.red_list))
    if spawn.b_count != 0:
        bullet(random.choice(spawn.blue_list))


# Random movement
def movement(red, blue):
    r_turtle = random.choice(red)
    if 20 < r_turtle.heading() < 340:
        r_turtle.seth(random.randrange(0, 25))
    r_turtle.left(random.randrange(-25, 25))
    r_turtle.forward(random.randrange(4, 10))
    if r_turtle.pos()[0] < -350 or r_turtle.pos()[1] > 200 or r_turtle.pos()[1] < -200:
        r_turtle.goto(random.randrange(-350, -125), random.randrange(-200, 200))
    b_turtle = random.choice(blue)
    b_turtle.forward(random.randrange(4, 10))
    if b_turtle.pos()[0] > 350 or b_turtle.pos()[1] > 200 or b_turtle.pos()[1] < -200:
        b_turtle.goto(random.randrange(125, 350), random.randrange(-200, 200))
    b_turtle.seth(random.randrange(155, 205))


# Main bullet function
def bullet(shooter):
    if random.randrange(0, 100) <= 10:
        bul = shooter.clone()
        bul.color("black")
        bul.seth(shooter.heading())
        travel = 0
        while travel < 550:
            bul.forward(5)
            bul.pos()
            travel += 5
            if bul.pos()[0] > 350 or bul.pos()[0] < -350 or bul.pos()[1] > 200 or bul.pos()[1] < -200:
                break
        if random.randrange(3) == 1:
            make_real_bullet(bul, shooter, spawn.red_list, spawn.blue_list)
        else:
            bul.hideturtle()
            bul.clear()
            del bul
    else:
        pass


# Bullet / soldier destruction
def make_real_bullet(bul, shooter, red_list, blue_list):
    if shooter.color()[0] == "red":
        target = random.choice(blue_list)
        bul.seth(bul.towards(target.pos()))
        for _ in range(10):
            bul.color("orange")
            time.sleep(0.1)
            bul.color("black")
        bul.pendown()
        bul.speed(10000)
        bul.goto(target.pos())
        bul.clear()
        target.clear()
        bul.hideturtle()
        target.hideturtle()
        spawn.blue_list.remove(target)
        spawn.b_count -= 1
    elif shooter.color()[0] == "blue":
        target = random.choice(red_list)
        bul.seth(bul.towards(target.pos()))
        for _ in range(20):
            bul.color("orange")
            time.sleep(0.1)
            bul.color("black")
        bul.pendown()
        bul.speed(10000)
        bul.goto(target.pos())
        bul.clear()
        target.clear()
        bul.hideturtle()
        target.hideturtle()
        spawn.red_list.remove(target)
        spawn.r_count -= 1


screen = turtle.Screen()
# Start
# noinspection PyUnresolvedReferences
if __name__ == '__main__':
    spawn(int(screen.numinput("Soldiers", "How many soldiers?", 7, 1, 100)))
    while spawn.r_count > 0 and spawn.b_count > 0:
        main()
    turtle.clearscreen()
    del spawn.red_list
    del spawn.blue_list
    explosion = []
    if spawn.r_count == 0:
        turtle.write("Blue Wins!", font=("Arial", 30, "normal"), align="center")
        while True:
            firework = turtle.Turtle()
            firework.color("blue")
            firework.penup()
            firework.seth(90)
            firework.goto(random.randrange(-275, 275), -100)
            firework.speed(1)
            firework.forward(random.randrange(200, 350))
            firework.hideturtle()
            count = random.randrange(6, 9)
            for _ in range(count):
                explosion.append(firework.clone())
            angle = 360 / count
            increment = 0
            for _ in explosion:
                _ = firework.clone()
                _.color("blue")
                _.pendown()
                _.speed(10)
                if angle * increment == 360:
                    break
                _.left(angle * increment)
                _.forward(random.randrange(25, 40))
                increment += 1
                _.penup()
                _.hideturtle()
            firework.hideturtle()
    elif spawn.b_count == 0:
        turtle.write("Red Wins!", font=("Arial", 30, "normal"), align="center")
        while True:
            firework = turtle.Turtle()
            firework.color("red")
            firework.penup()
            firework.seth(90)
            firework.goto(random.randrange(-275, 275), -100)
            firework.speed(1)
            firework.forward(random.randrange(200, 350))
            count = random.randrange(6, 9)
            firework.hideturtle()
            for _ in range(count):
                explosion.append(firework.clone())
            angle = 360 / count
            increment = 0
            for _ in explosion:
                _ = firework.clone()
                _.color("red")
                _.pendown()
                _.speed(10)
                if angle * increment == 360:
                    break
                _.left(angle * increment)
                _.forward(random.randrange(25, 40))
                increment += 1
                _.penup()
                _.hideturtle()
            firework.hideturtle()

turtle.done()
