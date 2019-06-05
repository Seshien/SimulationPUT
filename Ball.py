import tkinter as tk
import random
from tkinter import ttk
from tkinter import Canvas

class Ball2:
    def __init__(self, canvas, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1+5
        self.y2 = y1+5
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = random.randint(-5,5)
        deltay = random.randint(-5,5)
        self.canvas.move(self.ball, deltax, deltay)
