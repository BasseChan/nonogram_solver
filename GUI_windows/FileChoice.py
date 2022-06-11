from tkinter import *
from tkinter import messagebox
from Worktools.FileReader import read

class FileChoice:
    def __init__(self, master, back, toDataVerification):
        self.back = back
        self.toDataVerification = toDataVerification

        self.frame = Frame(master)
        self.frame.pack()

        self.back_button = Button(self.frame, text="Powrót", command=self.back_to_source_choice, height=2, width=8)
        self.back_button.grid(row=0, column=0, sticky=W)

        self.info_button = Button(self.frame, text="info", command=self.show_instruction, height=2, width=8)
        self.info_button.grid(row=0, column=2)

        self.info = Label(self.frame, text="Podaj pełną lokalizację pliku", height=2)
        self.info.grid(row=1, column=0, columnspan=3)

        self.localisation = Entry(self.frame, width=40)
        self.localisation.grid(row=2, column=0, columnspan=3)

        self.ok_button = Button(self.frame, text='Zatwierdź', height=2, width=15, command=self.read_and_go)
        self.ok_button.grid(row=3, column=0, columnspan=3)

    def show_instruction(self):
        messagebox.showinfo("Format plików", "Wgrywany plik musi być w odpowiednim formacie\n\n"
                                             "W pierwszej linijce podaj liczbę wierszy\n"
                                             "W drugiej linijce podaj liczbę kolumn\n\n"
                                             "Następnie podawaj ciągi czarnych pól po kolei dla każdego wiersza "
                                             "w osobnych linijkach\n\n"
                                             "Jeżeli w danym wierszu nie ma żadnego czarnego pola koniecznie podaj "
                                             "pustą linijkę\n\n"
                                             "Następnie podaj w analogiczny sposób wszystkie kolumny\n\n"
                                             "Nie dostawiaj nigdzie zbędnych pustych linii")

    def read_and_go(self):
        n, m, rows, columns = read(self.localisation.get())
        if not n == -1:
            self.frame.destroy()
            self.toDataVerification(n, m, rows, columns)

    def back_to_source_choice(self):
        self.frame.destroy()
        self.back()