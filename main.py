import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import messagebox
from Ball import *
from Graph import *
import math
import random
import numpy
import math

#1 Szerokosc okna
WIDTH = 800
# Wysokosc okna
HEIGHT = 640

#1 Szerokosc okna
WIDTHMAP = 780
# Wysokosc okna
HEIGHTMAP = 560
#Promien cząsteczki
RADIUS = 5 #2.5
#Szybkosc maksymalna czasteczek (ta wartosc / 2)
SPEED = 10 # 50

# Czy mozna rozszerzac
RESIZABLE = 0

# Zmienna odpowiadajaca za dzielenie na sektory od <-R, R>
R = 5


class Simulation:
    def __init__(self):
        # Lista wszystkich czasteczek
        self.particles = []
        self.running=0
        self.borderx=200
        self.bordery=200
        self.create_window()

    def create_window(self):
        # Tworzy nowe okno klasy Tk
        self.window = tk.Tk()
        # Ustawia nazwe okienka
        self.window.title("Projekt Fizyka")
        # Ustalenie wymiaru okienka za pomoca stringa "szerokoscxdlugosc"
        self.window.geometry(str(WIDTH) + "x" + str(HEIGHT))
        # Zabrania uzytkownikowi rozszerzania okna recznie
        self.window.resizable(RESIZABLE, RESIZABLE)
        # Utworzenie prostego napisu
        text = ttk.Label(self.window, text="Symulacja", width=10)
        # Umieszcza napis w oknie
        text.pack()
        # Utworzenie miejsca do rysowania
        self.canvas = Canvas(self.window, width=WIDTHMAP, height=HEIGHTMAP, bg="#4bf2a7")#, borderwidth=2, relief="ridge")
        # Umieszczenia miejsca w oknie
        self.canvas.pack()
        self.borders = self.canvas.create_rectangle(0, 0, self.borderx+RADIUS, self.bordery+RADIUS)
        add = ttk.Button(text="Dodaj",
                           command=lambda: self.add_click(number_input.get()))
        add.pack(side="right", padx=10)
        changeborders = ttk.Button(text="Granice",
                           command=lambda: self.change_click())
        changeborders.pack(side="right", padx=10)
        start = ttk.Button(text="Start/Stop",
                           command=lambda: self.start_click())
        start.pack(side="right", padx=10)
        reset = ttk.Button(text="Reset",
                           command=lambda: self.reset_click())
        reset.pack(side="right", padx=10)
        graph = ttk.Button(text="Wykres",
                           command=lambda: self.graph_click())
        graph.pack(side="right", padx=10)

        text_ilosc = ttk.Label(self.window, text="Ilość cząsteczek:")
        text_ilosc.pack(side="left", padx=50)
        # Entry to pole do wpisywania
        number_input = ttk.Entry(self.window)
        number_input.pack(side="left")
        number_input.insert(0, "10")
        self.refresh()
        self.window.mainloop()

    def add_click(self,number):
        print("Add clicked")
        self.add_new_particles(number)

    def start_click(self):
        print("Start clicked")
        if self.running == 0:
            self.running = 1

        elif self.running == 1:
            self.running = 0

    def reset_click(self):
        print("Reset clicked")
        self.running=0
        self.particles.clear()
        self.window.destroy()
        self.borderx=WIDTHMAP
        self.bordery=HEIGHTMAP
        self.create_window()

    def graph_click(self):
        print("Graph clicked")
        self.running=0
        Graph(self)

    def change_click(self):
        window = tk.Tk()
        text = ttk.Label(window, text="Podaj wartosci X i Y", width=20)
        text.pack()
        window.title("Podaj wartosci")
        window.geometry("400x100")
        window.resizable(RESIZABLE, RESIZABLE)
        x_input = ttk.Entry(window)
        x_input.pack(side="left", padx=10)
        x_input.insert(0, str(self.borderx))
        y_input = ttk.Entry(window)
        y_input.pack(side="left", padx=10)
        y_input.insert(0, str(self.bordery))
        ok = ttk.Button(window, text="OK",
                           command=lambda: self.change_ok_click(window, int(x_input.get()), int(y_input.get())))
        ok.pack(side="right", padx=10)

    def change_ok_click(self, window, x, y):
        self.borderx=x
        self.bordery=y
        window.destroy()
        for ball in self.particles:
            ball.change_limits(x, y)
        self.canvas.delete(self.borders)
        self.borders = self.canvas.create_rectangle(0, 0, self.borderx+RADIUS, self.bordery+RADIUS)

    def add_new_particles(self,number):
        try:
            number_of_particles = int(number)
        except ValueError:
            # Jesli nie to pokazuje blad i konczy prace programu
            messagebox.showerror("Błąd!", "Jako ilość cząsteczek nie podano wartości liczbowej!")
            self.window.destroy()
        # Na razie tylko wyswietla, to trzeba bedzie zastapic tworzeniem obiektow danej klasy
        #for i in range(number_of_particles):
        #    temp1 = random.randrange(0, self.borderx)
        #    temp2 = random.randrange(0, self.bordery)
        #    self.particles.append(Ball2(self.canvas, temp1, temp2, self.borderx, self.bordery))
        # Generowanie czasteczek na odpowiednich miejscach
        sector_width = self.borderx/(R*2+1)
        sector_height = self.bordery
        print("sector_width: ", sector_width)
        print("sector_height: ", sector_height)
        # Ilosc czasteczek w rzedzie
        old_number_x = int(math.sqrt(number_of_particles))
        old_number_y = math.ceil(number_of_particles/old_number_x)
        number_x = math.ceil(old_number_y * old_number_x / (R*2+1))
        number_y = math.ceil((old_number_y * (R*2+1))/old_number_x)

        print("number_x:", number_x, "number_y:", number_y)
        # Przemieszczenie czasteczki wzgledem innej czasteczki w poziomie lub w pionie w chwili startu
        offset_x = (sector_width - number_x * RADIUS * 2)/(number_x+1)
        offset_y = (sector_height - number_y * RADIUS * 2)/(number_y+1)
        print("offset_x:", offset_x, "offset_y:", offset_y)
        utworzone_czasteczki = 0
        #self.particles.append(Ball2(self.canvas, 0, 0, self.borderx, self.bordery))
        for j in range(number_x):
            for i in range(number_y):
                self.particles.append(Ball2(self.canvas, ((j+1) * offset_x) + j * RADIUS * 2 , ((i+1) * offset_y) + i * RADIUS * 2, self.borderx, self.bordery))
                utworzone_czasteczki += 1
                if number_of_particles <= utworzone_czasteczki:
                    break
            if number_of_particles <= utworzone_czasteczki:
                break

    def return_particles(self):
        return self.particles

    def check_collisions(self):
        if self.running==1:
            for i in range(len(self.particles)):
                for j in range(i+1, len(self.particles)):
                    if self.particles[i].check_coll(self.particles[j]):
                        self.have_collided(i, j)
                self.particles[i].move_ball()

    def refresh(self):
        if self.running==1:
            self.check_collisions()
        self.canvas.after(100, self.refresh)

    # Tu trzeba napisac kolidowanie
    def have_collided(self, i, j):
        ball1 = self.particles[i]
        ball2 = self.particles[j]
        ball1speed = numpy.array([ball1.x2, ball1.y2])
        ball2speed = numpy.array([ball2.x2, ball2.y2])
        vectordist = numpy.array([ball1.x1-ball2.x1, ball1.y1-ball2.y1])
        distanceSquared = vectordist[0] * vectordist[0] + vectordist[1] * vectordist[1]

        FirstParallel = (ball1speed[0] * vectordist[0] + ball1speed[1] * vectordist[1]) / distanceSquared * vectordist
        SecondParallel = (ball2speed[0] * vectordist[0] + ball2speed[1] * vectordist[1]) / distanceSquared * vectordist
        FirstPerpendicular = ball1speed - FirstParallel
        SecondPerpendicular = ball2speed - SecondParallel

        if (SecondParallel - FirstParallel)[0] * vectordist[0] < 0 or (SecondParallel - FirstParallel)[1] * vectordist[1] < 0:
            #print(ball1speed, ball2speed, (ball1speed+ball2speed)[0] + (ball1speed+ball2speed)[1])
            ball1speed = FirstPerpendicular + SecondParallel
            ball2speed = SecondPerpendicular + FirstParallel
            ball1.x2 = ball1speed[0]
            ball1.y2 = ball1speed[1]
            ball2.x2 = ball2speed[0]
            ball2.y2 = ball2speed[1]
            #print(ball1speed, ball2speed, (ball1speed+ball2speed)[0] + (ball1speed+ball2speed)[1])
        self.particles[i].change_color_blue()
        self.particles[j].change_color_blue()


def main():
    simulation = Simulation()

if __name__ == "__main__":
    main()
