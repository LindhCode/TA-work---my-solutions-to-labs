from tkinter import *
from model import *

root = Tk()

canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

o = canvas.create_oval(0, 30, 140, 150, fill="green")




# Task (8/12): Define a new function to_canvas_coords(canvas, x)

def to_canvas_coords(canvas, u: Vec):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    x_canvas = (h/20) * u.x + w/2
    y_canvas = (h/20) * -u.y + h/2
    return Vec(x_canvas, y_canvas)


# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(o, u1, u2):
    u1_canvas = to_canvas_coords(canvas, u1)
    u2_canvas = to_canvas_coords(canvas, u2)

    x0 = u1_canvas.x
    x1 = u2_canvas.x

    y0 = u1_canvas.y
    y1 = u2_canvas.y

    canvas.coords(o, x0, y0, x1, y1)

# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle: Particle):
    oval = canvas.create_oval(0, 0, 0, 0, fill="blue")
    u1,u2 = particle.bounding_box()
    move_oval_to(oval, u1, u2)
    return oval

# Task (7/12): Draw on canvas
import time


# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    parts = []
    for i in particles:
        parts.append(create_oval(canvas, i))
    f(timestep, particles)
    for j in particles:
        j.inertial_move(timestep)
        u1,u2 = j.bounding_box()
        move_oval_to(j, u1, u2)
    canvas.update()


input()



