# !usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Shooter:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name: %s" % self.name)

    def shoot(self):
        flag = random.randint(0, 2)
        if flag == 0:
            direction = "left"
        elif flag == 1:
            direction = "middle"
        else:
            direction = "right"

        print("%s shoots %s" % (self.name, direction))
        return direction


class Goalkeeper:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name: %s" % self.name)

    def save(self):
        flag = random.randint(0, 2)
        if flag == 0:
            direction = "left"
        elif flag == 1:
            direction = "middle"
        else:
            direction = "right"

        print("%s saves %s" % (self.name, direction))
        return direction

kicker = Shooter("Cristiano Ronaldo")
keeper = Goalkeeper("Manuel Neuer")
print(kicker.name)
keeper.display_name()
if kicker.shoot() == keeper.save():
    print("What a save!")
else:
    print("What a goal!")