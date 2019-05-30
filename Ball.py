import tkinter as tk
import random
from tkinter import ttk
from tkinter import Canvas

class Ball():
    # Wczytuje obrazek czasteczki
    #czasteczka_img = tk.PhotoImage(file="czasteczka.png")

    def __init__(self, xPos = 0, yPos = 0, r = 0, xSpeed = 0, ySpeed = 0,canvas=""):
        self.x = xPos
        self.y = yPos
        self.radius = r
        self.dx = xSpeed
        self.dy = ySpeed
        print("x")
        self.img = canvas.create_image(self.x, self.y, image=tk.PhotoImage(file="czasteczka.png"))

    def ruch(self):
        self.x += self.dx
        self.y += self.dy

    def draw (self,window,canvas):
        canvas.move(self.img,self.dx,self.dy)
        #canvas.after(50, self.draw(window,canvas))

    def collision(self, other, delta):
        odlegloscX = abs(self.x + other.x)
        odlegloscY = abs(self.y + other.y)

class Ball2:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = random.randint(-5,5)
        deltay = random.randint(-5,5)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)
