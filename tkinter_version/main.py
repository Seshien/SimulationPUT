import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import messagebox
from Ball import *
import random

#1 Szerokosc okna
WIDTH = 800
# Wysokosc okna
HEIGHT= 640
# Czy mozna rozszerzac
RESIZABLE = 0
class Simulation:
    def __init__(self):
        # Lista wszystkich czasteczek
        self.particles = []
        self.create_window()
        self.window.mainloop()


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
        self.canvas = Canvas(self.window, width=WIDTH - 20, height=HEIGHT - 80, bg="#4bf2a7", borderwidth=2, relief="ridge")
        # Umieszczenia miejsca w oknie
        self.canvas.pack()
        start = ttk.Button(text="Twórz",
                           command=lambda: self.button_click())
        start.pack(side="right", padx=50)
        text_ilosc = ttk.Label(self.window, text="Ilość cząsteczek:")
        text_ilosc.pack(side="left", padx=50)
        # Entry to pole do wpisywania
        number_input = ttk.Entry(self.window)
        number_input.pack(side="left")
        number_input.insert(0, "10")

    def button_click(self):
        print("Something")

def create_random(particles, window,canvas):
     particles.append(Ball(random.randrange(0, WIDTH-20), random.randrange(0, HEIGHT-80), 5, random.randrange(-5, 5), random.randrange(-5, 5),canvas))

def redraw(window,canvas,particles):
    print("Tada")
    for particle  in particles:
        particle.draw(window,canvas)


def simulation_start(number_of_particles, window, canvas, particles):
    # Sprawdza czy uzytkownik podal odpowiednia wartosc jako ilosc czasteczek
    try:
        number_of_particles = int(number_of_particles)
    except ValueError:
        # Jesli nie to pokazuje blad i konczy prace programu
        messagebox.showerror("Błąd!", "Jako ilość cząsteczek nie podano wartości liczbowej!")
        window.destroy()
    # Na razie tylko wyswietla, to trzeba bedzie zastapic tworzeniem obiektow danej klasy
    for i in range(number_of_particles):
        temp1 = random.randrange(0, 1000)
        temp2 = random.randrange(0, 1000)
        particles.append(Ball2(canvas,temp1,temp2,temp1+10,temp2+10))
        particles[i].move_ball()

def main():
    simulation = Simulation()

if __name__ == "__main__":
    main()
