import random
import turtle
import time
from threading import Thread


class RedSoldiers:
    def __init__(self, amt):
        self.soldiers = []
        self.amt = amt
        self.spawn()

    def spawn(self):
        for _ in range(self.amt):
            self.soldiers.append(turtle.Turtle())
        for s in self.soldiers:
            s.color("red")
            s.penup()
            s.goto(random.randrange(-350, -125), random.randrange(-200, 200))
            s.seth(0)

    def movement(self):
        for s in self.soldiers:
            s.forward(random.randrange(1, 5))
            s.left(random.randrange(-25, 25))
            if s.heading() > 340 or s.heading() < 20:
                s.seth(random.randrange(0, 25))
            if s.pos()[0] > 350 or s.pos()[0] < -350 or s.pos()[1] > 200 or s.pos()[1] < -200:
                s.goto(random.randrange(-350, -125), random.randrange(-200, 200))
                s.seth(0)
        if random.randrange(100) == 1:
            Bullet(random.choice(self.soldiers))


class BlueSoldiers:
    def __init__(self, amt):
        self.soldiers = []
        self.amt = amt
        self.spawn()

    def spawn(self):
        for _ in range(self.amt):
            self.soldiers.append(turtle.Turtle())
        for s in self.soldiers:
            s.color("blue")
            s.penup()
            s.goto(random.randrange(125, 350), random.randrange(-200, 200))
            s.seth(0)

    def movement(self):
        for s in self.soldiers:
            s.forward(random.randrange(0, 5))
            s.left(random.randrange(-25, 25))
            if s.heading() > 160 or s.heading() < 200:
                s.seth(random.randrange(0, 25))
            if s.pos()[0] > 350 or s.pos()[0] < -350 or s.pos()[1] > 200 or s.pos()[1] < -200:
                s.goto(random.randrange(350, 125), random.randrange(-200, 200))
                s.seth(0)
        if random.randrange(100) == 1:
            Bullet(random.choice(self.soldiers))


class Bullet:
    def __init__(self, shooter):
        self.shooter = shooter
        self.bul = self.shooter.clone()
        self.bul.color("black")
        self.bul.seth(self.shooter.heading())
        self.dist = 0
        self.travel()

    def travel(self):
        while self.dist < 550:
            self.bul.forward(5)
            self.bul.pos()
            self.travel += 5
            if self.bul.pos()[0] > 350 or self.bul.pos()[0] < -350 \
                    or self.bul.pos()[1] > 200 or self.bul.pos()[1] < -200:
                break
        if random.randrange(3) == 1:
            self.make_real_bullet("blue")
        else:
            self.bul.hideturtle()
            self.bul.clear()
            del self.bul

    def make_real_bullet(self, target_color):
        if target_color == "red":
            target = random.choice(RedSoldiers.soldiers)
            self.bul.seth(self.bul.towards(target.pos()))
            for _ in range(10):
                self.bul.color("orange")
                time.sleep(0.1)
                self.bul.color("black")
            self.bul.pendown()
            self.bul.speed(10000)
            self.bul.goto(target.pos())
            self.bul.clear()
            target.clear()
            self.bul.hideturtle()
            target.hideturtle()
            RedSoldiers.soldiers.remove(target)
        elif target_color == "blue":
            target = random.choice(BlueSoldiers.soldiers)
            self.bul.seth(self.bul.towards(target.pos()))
            for _ in range(20):
                self.bul.color("orange")
                time.sleep(0.1)
                self.bul.color("black")
            self.bul.pendown()
            self.bul.speed(10000)
            self.bul.goto(target.pos())
            self.bul.clear()
            target.clear()
            self.bul.hideturtle()
            target.hideturtle()
            BlueSoldiers.soldiers.remove(target)


screen = turtle.Screen()
# Start
# noinspection PyUnresolvedReferences
if __name__ == '__main__':
    RedSoldiers(10)
    BlueSoldiers(10)
    while RedSoldiers.soldiers and BlueSoldiers.soldiers:
        RedSoldiers.movement(RedSoldiers.soldiers)
        BlueSoldiers.movement(BlueSoldiers.soldiers)
    turtle.clearscreen()
    explosion = []
    if len(RedSoldiers.soldiers) == 0:
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
    elif len(BlueSoldiers.soldiers) == 0:
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
