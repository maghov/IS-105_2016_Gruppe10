# -*- coding: utf-8 -*-
from Tkinter import *
import time

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.venstre = Button(frame, text="Venstre", command=self.venstre)
        self.venstre.pack(side=LEFT)

        self.hoyre = Button(frame, text="Høyre", command=self.hoyre)
        self.hoyre.pack(side=LEFT)

        self.fox = Button(frame, text="Rev i båt", command=self.fox)
        self.fox.pack(side=LEFT)

        self.grain = Button(frame, text="Grain i båt", command=self.grain)
        self.grain.pack(side=LEFT)

        self.pig = Button(frame, text="Gris i båt", command=self.pig)
        self.pig.pack(side=LEFT)

    def hoyre(self):
    	for x in range(0, 100):
			canvas.move(1, 4, 0)
			root.update()
			time.sleep(0.02)


    def venstre(self):
        for x in range(0, 100):
			canvas.move(1, -4, 0)
			root.update()
			time.sleep(0.02)

    def fox(self):
        print "Hello world!"


    def grain(self):
        print "Hello world2!"

    def pig(self):
        print "Hello"


root = Tk()


canvas = Canvas(root, width=700, height=300)
canvas.pack()

boat = canvas.create_rectangle(100, 50, 200, 20, fill = "yellow")
water = canvas.create_rectangle(50, 100, 650, 50, fill = "blue")
leftSide = canvas.create_rectangle(0, 100, 100, 25, fill = "brown")
rightSide = canvas.create_rectangle(700, 100, 600, 25, fill = "brown")
fox = canvas.create_rectangle(10, 10, 20, 20, fill = "orange")
pig = canvas.create_rectangle(30, 10, 20, 20, fill = "red")
grain = canvas.create_rectangle(60, 10, 30, 20, fill ="green")





app = App(root)

root.mainloop()
root.destroy() # optional; see description below
