import tkinter as tk
import random
from tkinter import ttk
from tkinter import Canvas
#1 Szerokosc okna
WIDTHMAP = 775
# Wysokosc okna
HEIGHTMAP = 555

RADIUS = 2.5

BLISKOSC = 5


class Ball2:
    def __init__(self, canvas, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = random.randint(-25,25)
        self.y2 = random.randint(-25,25)
        self.r = RADIUS
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x1+5, self.y1+5, fill="red")

    def move_ball(self):
        wektorx=self.x2
        wektory=self.y2
        if self.y1+wektory>HEIGHTMAP:
            wektory = -(wektory-(HEIGHTMAP-self.y1))
            self.y2 = -self.y2
        if self.y1+wektory<5:
            wektory = -(wektory-(5-self.y1))
            self.y2 = -self.y2
        if self.x1+wektorx>WIDTHMAP:
            wektorx = -(wektorx-(WIDTHMAP-self.x1))
            self.x2 = -self.x2
        if self.x1+wektorx<5:
            wektorx = -(wektorx-(5-self.x1))
            self.x2 = -self.x2
        self.x1 += wektorx
        self.y1 += wektory
        self.canvas.move(self.ball, wektorx, wektory)

    def return_coordinates(self):
        return [self.x1, self.y1, self.x2, self.y2]
