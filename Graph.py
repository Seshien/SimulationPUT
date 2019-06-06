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


class Plot(tk.Tk):
    def __init__(self, fig):
        tk.Tk.__init__(self)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class Graph:
    def __init__(self, simulation):
        self.simulation=simulation
        fig = Figure(figsize=(6, 6), dpi=100)
        a = fig.add_subplot(111)
        app = Plot(fig)
        ani = animation.FuncAnimation(fig, self.animate, interval=25, blit=False)
        app.mainloop()

    def animate(self):
        # df = pd.read_csv('LogMati kopia.csv', skiprows=17)
        # x = df['X [ms]']
        # y = df
        balls = self.simulation.return_particles()
        # for ball in Balls:
        print(Balls)
        # a.clear()
        # a.plot(x,y)

