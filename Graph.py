import tkinter as tk
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use("ggplot")
import plotly.plotly
import plotly.graph_objs as go
import main

class Plot(tk.Tk):
    def __init__(self, fig):
        tk.Tk.__init__(self)
        self.title("Entropy")
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


class Graph:
    states = []
    x = []
    y = []
    time = 1 / 200
    j = 0

    def __init__(self, simulation):
        self.simulation = simulation
        fig = Figure(figsize=(6, 6), dpi=100)
        self.a = fig.add_subplot(111, title="Entropy", xlabel="tj", ylabel="S")

        app = Plot(fig)
        ani = animation.FuncAnimation(fig, self.animate, interval=25, blit=False)
        app.mainloop()
        if main.SAVE:
            # fig.savefig('Entropy.png')
            chart = []
            chart.append(go.Scatter(x=self.x, y=self.y, mode='lines', name="Entropy"))
            plotly.offline.plot({"data": chart,
                                 "layout": go.Layout(title="Entropy", xaxis={'title': 'tj'}, yaxis={'title': 'S'})},
                                filename="Entropy.html")

    def animate(self, i):
        if self.simulation.running == 1 and len(self.states):

            Number_of_particles = len(self.simulation.particles)
            nominator = Number_of_particles * math.log1p(Number_of_particles) - Number_of_particles

            for state in self.states:
                if state != 0:
                    denominator = state * math.log1p(state) - state
                    nominator -= denominator

            self.j += 1
            self.x.append(self.j * self.time)
            self.y.append(nominator)

            self.simulation.Entropy = nominator

            self.a.clear()
            self.a.plot(self.x, self.y)
            self.a.set_title("Entropy")
            self.a.set_xlabel("tj")
            self.a.set_ylabel("S")

