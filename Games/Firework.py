import tkinter as tk
from random import random, randint, seed
from time import time
from math import sqrt, pow

root = tk.Tk()
root.title('Happy new year')
canvas = tk.Canvas(root, width=800, height=800, bg='midnight blue')
canvas.pack()

colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'pink']

class Particle:
    def __init__(self, position, velocity, ttl, color, friction=0.95, gravity=0.5):
        self.position = position
        self.velocity = velocity
        self.ttl = ttl
        self.color = color

        self.size = random() * 10 + 1

        self.friction = friction
        self.gravity = gravity

        self.timer = time()

    def clock(self):
        if time() - self.timer >= self.ttl:
            self.timer = time()
            return True
        return False

    def update(self):
        if self.clock():
            particles.remove(self)

        self.size *= 0.99

        self.velocity[0] *= self.friction
        self.velocity[1] *= self.friction

        self.gravity *= self.friction

        self.velocity[1] += self.gravity

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self):
        canvas.create_oval(self.position[0], self.position[1], self.position[0] + self.size, self.position[1] + self.size, fill=self.color, outline='')


class Rocket:
    def __init__(self, position, angle, speed, explosion, ttl, gravity=0.05, newRocket=False):
        self.position = position
        self.explosion = explosion
        self.ttl = ttl
        self.gravity = gravity
        self.newRocket = newRocket

        self.velocity = [map(angle, -45, 45, -1, 1) * speed, -speed]

        self.timer = time()

    def clock(self):
        if time() - self.timer >= self.ttl:
            self.timer = time()
            return True
        return False

    def normalized(self):
        length = sqrt(pow(self.velocity[0], 2) + pow(self.velocity[1], 2))
        return [self.velocity[0] / length, self.velocity[1] / length]

    def update(self):
        if self.clock():#and self.velocity[1] > 0:
            if self.newRocket:
                for i in range(20):
                    rockets.append(Rocket(self.position, randint(0, 360) - 180, random(), randint(1, 5), random(), 0.05, False))

            for i in range(self.explosion):
                particles.append(Particle([self.position[0] + randint(10, 20) - 15, self.position[1] + randint(10, 20) - 15], [random() * 20 - 10, random() * 20 - 10], random() * 2, colors[randint(0, len(colors) - 1)]))

            rockets.remove(self)

        self.velocity[1] += self.gravity

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self):
        canvas.create_line(self.position[0], self.position[1], self.position[0] + self.normalized()[0] * 20, self.position[1] + self.normalized()[1] * 20, fill='grey80', width=5)


def map(value, x1, y1, x2, y2):
    return (value - x1) * (y2 - x2) / (y1 - x1) + x2


class Launcher:
    def __init__(self, position, frequency):
        self.position = position
        self.frequency = frequency

        self.timer = time()

    def clock(self):
        if time() - self.timer >= self.frequency:
            self.timer = time()
            return True
        return False

    def shoot(self):
        if self.clock():
            rockets.append(Rocket([400, 750], randint(0, 90) - 45, randint(4, 6) + random(), randint(10, 50), 1.5, 0.05, True))


particles = []
rockets = []

launcher = Launcher([400, 750], 1)


def main():
    while True:
        canvas.delete('all')
        for particle in particles:
            particle.update()
            particle.draw()

        for rocket in rockets:
            rocket.update()
            rocket.draw()

        launcher.shoot()

        root.update()
        canvas.after(10)


main()
root.mainloop()
