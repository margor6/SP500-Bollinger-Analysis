import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BollingerApp:
    def __init__(self, master):
        self.master = master
        master.title("Analiza S&P 500 - Wstęgi Bollingera")

        #Suwak do ustawienia długości okna
        self.window_label = tk.Label(master, text="Okno (dni):") 
        self.window_label.pack()

        self.window_slider = tk.Scale(master, from_=5, to=60, resolution=1, orient=tk.HORIZONTAL, 
                                      command=self.update_plot)
        self.window_slider.pack()
        self.window_slider.set(20)

        #Przycisk do załadowania danych
        self.load_button = tk.Button(master, text="Pobierz dane S&P 500", command=self.load_data)
        self.load_button.pack()

        #Przycisk wyjścia
        self.quit_button = tk.Button(master, text="Zamknij", command=self.Quit)
        self.quit_button.pack()

        #Wykres
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

        self.data = None

    def load_data(self):  #Pobieranie danych z Yahoo Finance
        try:
            symbol = "^GSPC"
            df = yf.download(symbol, period="12mo", interval="1d", auto_adjust=True)
            if df.empty:
                raise ValueError("Nie udało się pobrać danych.") #Info dla uzytkownika/oblusga bledow
            self.data = df
            messagebox.showinfo("Sukces", "Dane zostały pobrane pomyślnie.")
            self.update_plot()
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd przy pobieraniu danych: {e}")

    def update_plot(self, event=None):
        if self.data is None:
            return

        window = self.window_slider.get()

        df = self.data.copy()     #Liczymy potrzebne nam parametry i wstęgi, zgodnie z oknem od użytkownika
        df['Średnia krocząca'] = df['Close'].rolling(window=window).mean()
        df['STD'] = df['Close'].rolling(window=window).std()
        df['Upper'] = df['Średnia krocząca'] + (df['STD'] * 2)
        df['Lower'] = df['Średnia krocząca'] - (df['STD'] * 2)

        self.ax.clear()           #Ustalamy ich wyswietlanie, kolory itd
        self.ax.plot(df.index, df['Close'], label='Kurs zamknięcia', color='blue')
        self.ax.plot(df.index, df['Średnia krocząca'], label=f'Średnia krocząca {window}', color='orange')
        self.ax.plot(df.index, df['Upper'], label='Górna wstęga', color='green', linestyle='--')
        self.ax.plot(df.index, df['Lower'], label='Dolna wstęga', color='red', linestyle='--')
        self.ax.fill_between(df.index, df['Upper'], df['Lower'], color='gray', alpha=0.1)

        self.ax.set_title("Wstęgi Bollingera - S&P 500")   #Opisusjemy osie
        self.ax.set_xlabel("Data")
        self.ax.set_ylabel("Wartość (USD)")
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()

    def Quit(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BollingerApp(root)
    root.mainloop()