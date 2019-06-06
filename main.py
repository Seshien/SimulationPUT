import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import messagebox
from Ball import *
from Graph import *
import random

#1 Szerokosc okna
WIDTH = 800
# Wysokosc okna
HEIGHT = 640

#1 Szerokosc okna
WIDTHMAP = 780
# Wysokosc okna
HEIGHTMAP = 560

# Czy mozna rozszerzac
RESIZABLE = 0


class Simulation:
    def __init__(self):
        # Lista wszystkich czasteczek
        self.particles = []
        self.running=0
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
        self.canvas = Canvas(self.window, width=WIDTHMAP, height=HEIGHTMAP, bg="#4bf2a7", borderwidth=2, relief="ridge")
        # Umieszczenia miejsca w oknie
        self.canvas.pack()

        add = ttk.Button(text="Dodaj",
                           command=lambda: self.add_click(number_input.get()))
        add.pack(side="right", padx=10)
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
        self.create_window()

    def graph_click(self):
        print("Graph clicked")
        self.running=0
        graph_main(self)

    def add_new_particles(self,number):
        try:
            number_of_particles = int(number)
        except ValueError:
            # Jesli nie to pokazuje blad i konczy prace programu
            messagebox.showerror("Błąd!", "Jako ilość cząsteczek nie podano wartości liczbowej!")
            self.window.destroy()
        # Na razie tylko wyswietla, to trzeba bedzie zastapic tworzeniem obiektow danej klasy
        for i in range(number_of_particles):
            temp1 = random.randrange(0, WIDTH - 20)
            temp2 = random.randrange(0, HEIGHT - 80)
            self.particles.append(Ball2(self.canvas, temp1, temp2))

    def return_particles(self):
        return self.particles

    def check_collisions(self):
        if self.running==1:
            for i in range(len(self.particles)):
                for j in range(i+1, len(self.particles)):
                    if self.particles[i].check_coll(self.particles[j]):
                        self.have_collided(i, j)

    def check_collision(self,i):
            for j in range(i+1, len(self.particles)):
                    if self.particles[i].check_coll(self.particles[j]):
                        return j
            return -1

    def refresh(self):
        if self.running==1:
            for i in range(len(self.particles)):
                j = self.check_collision(i)
                if j ==- 1:
                    self.particles[i].move_ball()
                else:
                    self.have_collided(i, j)
        self.canvas.after(10, self.refresh)

    # Tu trzeba napisac kolidowanie
    def have_collided(self, i, j):

        pass


def main():
    simulation = Simulation()

if __name__ == "__main__":
    main()
