#!/usr/bin/env pytest
import tkinter as tk
from tkinter import scrolledtext as scrolledtext

class Calculator(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def calculate(self):
        print('Calculate')

    def clearButtonInput(self):
        print('Clear')

    def zeroButtonInput(self):
        print('0')

    def oneButtonInput(self):
        print('1')

    def twoButtonInput(self):
        print('2')

    def threeButtonInput(self):
        print('3')

    def fourButtonInput(self):
        print('4')

    def fiveButtonInput(self):
        print('5')

    def sixButtonInput(self):
        print('6')

    def sevenButtonInput(self):
        print('7')

    def eightButtonInput(self):
        print('8')

    def nineButtonInput(self):
        print('9')

    def plusButtonInput(self):
        print('+')

    def minusButtonInput(self):
        print('-')

    def createWidgets(self):

        # Construct widget
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.calculateButton = tk.Button(self, text='Calculate', command=self.calculate)
        self.clearButton = tk.Button(self, text='Clear', command=self.clearButtonInput)
        self.zeroButton = tk.Button(self, text='0', command=self.zeroButtonInput)
        self.oneButton = tk.Button(self, text='1', command=self.oneButtonInput)
        self.twoButton = tk.Button(self, text='2', command=self.twoButtonInput)
        self.threeButton = tk.Button(self, text='3', command=self.threeButtonInput)
        self.fourButton = tk.Button(self, text='4', command=self.fourButtonInput)
        self.fiveButton = tk.Button(self, text='5', command=self.fiveButtonInput)
        self.sixButton = tk.Button(self, text='6', command=self.sixButtonInput)
        self.sevenButton = tk.Button(self, text='7', command=self.sevenButtonInput)
        self.eightButton = tk.Button(self, text='8', command=self.eightButtonInput)
        self.nineButton = tk.Button(self, text='9', command=self.nineButtonInput)
        self.plusButton = tk.Button(self, text='+', command=self.plusButtonInput)
        self.minusButton = tk.Button(self, text='-', command=self.minusButtonInput)
        self.textField = scrolledtext.ScrolledText(self, width=15, height=10)

        # Place widget
        self.textField.grid(row=0, column=3, rowspan=3)
        self.zeroButton.grid(row=3, column=0)
        self.clearButton.grid(row=3, column=1)
        self.calculateButton.grid(row=3, column=2)
        self.quitButton.grid(row=3, column=3)
        self.oneButton.grid(row=2, column=0)
        self.twoButton.grid(row=2, column=1)
        self.threeButton.grid(row=2, column=2)
        self.fourButton.grid(row=1, column=0)
        self.fiveButton.grid(row=1, column=1)
        self.sixButton.grid(row=1, column=2)
        self.sevenButton.grid(row=0, column=0)
        self.eightButton.grid(row=0, column=1)
        self.nineButton.grid(row=0, column=2)




app = Calculator()
app.master.title('Calculator')
app.mainloop()

