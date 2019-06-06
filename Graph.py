import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # , NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

style.use("ggplot")

#import numpy as np
#import pandas as pd

import main

# 1 Szerokosc okna
WIDTH = 800
# Wysokosc okna
HEIGHT = 640

fig = Figure(figsize=(6, 6), dpi=100)
a = fig.add_subplot(111)


def animate(i):
    # df = pd.read_csv('LogMati kopia.csv', skiprows=17)
    # x = df['X [ms]']
    # y = df
    sim = main.Simulation()
    Balls = sim.return_particles()
    # for ball in Balls:
    print(Balls)
    # a.clear()
    # a.plot(x,y)


class Plot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


def graph_main(simulation):
    app = Plot()
    ani = animation.FuncAnimation(fig, animate, interval=25, blit=False)
    app.mainloop()
