from tkinter import *
from GUI_windows.SourceChoice import SourceChoice
from GUI_windows.SizeChoice import SizeChoice
from GUI_windows.FileChoice import FileChoice
from GUI_windows.PassData import PassData
from GUI_windows.Field import Field


class GUI:
    def __init__(self):
        self.root = Tk()
        self.sourceChoice()
        self.root.mainloop()

    def sourceChoice(self):
        self.root.title("Wybór źródła danych")
        SourceChoice(self.root, self.readFromFile, self.sizeChoice)

    def sizeChoice(self):
        self.root.title("Wybór rozmiaru")
        SizeChoice(self.root, self.sourceChoice, self.passData)

    def passData(self, n, m, rows=None, columns=None):
        self.root.title("Wpisywanie danych")
        PassData(self.root, n, m, self.sourceChoice, self.field, rows, columns)

    def readFromFile(self):
        self.root.title("Czytanie z pliku")
        FileChoice(self.root, self.sourceChoice, self.passData)

    def field(self, n, m, rows, columns):
        self.root.title("Plansza")
        Field(self.root, n, m, rows, columns, self.sourceChoice, self.passData)

GUI()