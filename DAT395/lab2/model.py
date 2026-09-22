import math
# Task (2/12): Define a class Vec
class Vec():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __rmul__(self,factor):
        return Vec(self.x*factor, self.y*factor)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def get_coords(self):
        return (self.x, self.y)


# Task (3/12): Additionally define a function dot(u, v)
def dot(u,v):
    return (u.x*v.x + u.y*v.y)


# Task (4/12): Create a class Particle
class Particle():
    def __init__(self, mass, position: Vec, velocity: Vec, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius

    # Task (5/12): In the Particle class, implement a method inertial_move(self, dt).
    def inertial_move(self, dt):
        self.position = self.position + dt * self.velocity

    # Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)
    def apply_force(self, dt, f):
        self.velocity = self.velocity + dt/self.mass * f


# Task (9/12): In the Particle class, add a method bounding_box(self)
    def bounding_box(self):
        top_left = Vec(self.position.x - self.radius, self.position.y + self.radius)
        bot_right = Vec(self.position.x + self.radius, self.position.y - self.radius)
        return top_left, bot_right



###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################