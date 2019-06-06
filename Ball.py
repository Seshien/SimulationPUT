import tkinter as tk
import random
from tkinter import ttk
from tkinter import Canvas
RADIUS = 10
#1 Szerokosc okna
WIDTHMAP = 780 - RADIUS
# Wysokosc okna
HEIGHTMAP = 560 - RADIUS



BLISKOSC = 5


class Ball2:
    def __init__(self, canvas, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = random.randint(-25,25)
        self.y2 = random.randint(-25,25)
        self.r = RADIUS
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x1+(self.r*2), self.y1+(self.r*2), fill="red")

    def move_ball(self):
        wektorx=self.x2
        wektory=self.y2
        if self.y1+wektory>HEIGHTMAP:
            wektory = -(wektory-(HEIGHTMAP-self.y1))
            self.y2 = -self.y2
        if self.y1+wektory<self.r:
            wektory = -(wektory-(self.r-self.y1))
            self.y2 = -self.y2
        if self.x1+wektorx>WIDTHMAP:
            wektorx = -(wektorx-(WIDTHMAP-self.x1))
            self.x2 = -self.x2
        if self.x1+wektorx<self.r:
            wektorx = -(wektorx-(self.r-self.x1))
            self.x2 = -self.x2
        self.x1 += wektorx
        self.y1 += wektory
        self.canvas.move(self.ball, wektorx, wektory)

    def check_coll(self, other):
        delta = self.r*0.01
        odl_srodki = ((self.x1+self.r - other.x1+other.r)+(self.y1+self.r - other.y1+other.r))**2
        if odl_srodki > abs(self.r - other.r) and odl_srodki < abs(self.r + other.r):
            #print("Collision!")
            return True
        return False
            

    def return_coordinates(self):
        return [self.x1, self.y1, self.x2, self.y2]
