import random
from math import sqrt

class Rocket():
    """Creates rockets that can move in x and y directions"""

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move_up(self, x_increment = 0, y_increment = 1):
        self.x += x_increment
        self.y += y_increment
        return self.x, self.y

    def get_distance(self, other_rocket):
        return sqrt((other_rocket.get_x()-self.x)**2 + (other_rocket.get_y()-self.y)**2)

    def __str__(self):
        return "Rocket is moving in %dx and %dy directions." %(self.get_x(), self.get_y())

# create a fleet of rockets
rocket_fleet = []
for num in range(5):
    rocket_fleet.append(Rocket(x = 0, y = 0))

# make my rockets move around
sideways = 0
up_or_down = 0
for rocket in rocket_fleet:
    sideways += random.random()*10
    up_or_down += random.random()*100
    rocket.move_up(x_increment = sideways, y_increment = up_or_down)
    print (rocket)

# compute distances between the rockets in my fleet
distance = 0
for index1, rocket_x in enumerate(rocket_fleet):
    for index2, rocket_y in enumerate(rocket_fleet):
        if index2 <= index1:
            pass
        else:
            distance = rocket_x.get_distance(rocket_y)
            print (f"Distance between rocket {index1} and rocket {index2} is {distance:0.2f}.") # reminder: use 0.2f for precision
        
    
