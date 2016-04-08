# -*- coding: utf-8 -*-
from Tkinter import *
import time



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

fox1 = 0
grain1 = 0
pig1 = 0

#Tilstand 1 = Venstre side
#Tilstand 2 = Høyre side

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


    def venstre(self):
        for x in range(0, 100):
            canvas.move(1, -4, 0)
            root.update()
            time.sleep(0.02)

    def fox(self):
        if fox1 == 0:
            for x in range(0, 10):
                canvas.move(5, 10, 0)
                root.update()
                time.sleep(0.02)
            global fox1
            fox1 = 1
            print fox1
        elif fox1 == 1:
            for x in range(0, 10):
                canvas.move(5, 10, 0)
                root.update()
                time.sleep(0.02)
            global fox1
            fox1 = 2
            print fox1


    def grain(self):
        if grain1 == 0:
            for x in range(0, 10):
                canvas.move(7, 10, 0)
                root.update()
                time.sleep(0.02)
            global grain1
            grain1 = 1
        elif grain1 == 1:
                for x in range(0, 10):
                    canvas.move(7, 10, 0)
                    root.update()
                    time.sleep(0.02)
                global grain1
                grain1 = 2
                print grain1

    def pig(self):
        if pig1 == 0:
            for x in range(0, 10):
                canvas.move(6, 10, 0)
                root.update()
                time.sleep(0.02)
            global pig1
            pig1 = 1
        elif pig1 == 1:
                for x in range(0, 10):
                    canvas.move(6, 10, 0)
                    root.update()
                    time.sleep(0.02)
                global pig1
                pig1 = 2
                print pig1


    def hoyre(self):
        if fox1 == 1:
           for x in range(0, 100):
                canvas.move(1, 4, 0)
                canvas.move(5, 4, 0)
                root.update()
                time.sleep(0.02)
        elif grain1 == 1:
            for x in range(0, 100):
                canvas.move(1, 4, 0)
                canvas.move(7, 4, 0)
                root.update()
                time.sleep(0.02)
        elif pig1 == 1:
            for x in range(0, 100):
                canvas.move(1, 4, 0)
                canvas.move(6, 4, 0)
                root.update()
                time.sleep(0.02)
        else:
            for x in range(0, 100):
                 canvas.move(1, 4, 0)
                 root.update()
                 time.sleep(0.02)










app = App(root)

root.mainloop()
root.destroy() # optional; see description below
