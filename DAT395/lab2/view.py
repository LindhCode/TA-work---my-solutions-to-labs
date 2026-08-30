from tkinter import *
from model import *

root = Tk()

canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

o = canvas.create_oval(80, 30, 140, 150, fill="green")

# Task (7/12): Draw on canvas
input()

# Task (8/12): Define a new function to_canvas_coords(canvas, x)

def to_canvas_coords(canvas, u: Vec):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    x_canvas = (h/20) * u.x + w/2
    y_canvas = (h/20) * -u.y + h/2
    return Vec(x_canvas, y_canvas)

#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)

# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)