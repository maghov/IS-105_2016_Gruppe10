# -*- coding: utf-8 -*-
from Tkinter import *
#import time

root = Tk()

canvas = Canvas(root, width=700, height=300)
canvas.pack()
# Lager de forskjellige "boksene"
boat = canvas.create_rectangle(100, 50, 200, 20, fill = "green")
water = canvas.create_rectangle(50, 100, 650, 50, fill = "blue")
leftSide = canvas.create_rectangle(0, 100, 100, 25, fill = "brown")
rightSide = canvas.create_rectangle(700, 100, 600, 25, fill = "brown")
fox = canvas.create_rectangle(10, 10, 20, 20, fill = "red")
pig = canvas.create_rectangle(30, 10, 20, 20, fill = "pink")
grain = canvas.create_rectangle(60, 10, 30, 20, fill ="yellow")
# Setter "tilstanden" til de forskjellige elementene til 0
fox1 = 0
grain1 = 0
pig1 = 0
boat1= 0

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
# Koden til de forskjellige knappene.
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.venstre = Button(frame, text="Venstre", command=self.venstre)
        self.venstre.pack(side=LEFT)
        self.venstre.configure(state=DISABLED)

        self.hoyre = Button(frame, text="Høyre", command=self.hoyre)
        self.hoyre.pack(side=LEFT)

        self.fox = Button(frame, text="Rev inn/ut av båt", command=self.fox)
        self.fox.pack(side=LEFT)

        self.grain = Button(frame, text="Grain inn/ut av båt", command=self.grain)
        self.grain.pack(side=LEFT)

        self.pig = Button(frame, text="Gris inn/ut av båt", command=self.pig)
        self.pig.pack(side=LEFT)

#================================================================
    def venstre(self): # Funksjon for venstre knappen
        global boat1
        boat1 = 0      # Setter tilstanden til boat1 til 0
        print boat1
        if fox1 == 3:
           for x in range(0, 100):
                canvas.move(1, -4, 0)
                canvas.move(5, -4, 0)
                root.update()
                time.sleep(0.02)
                global fox1
                fox1 = 1
                print fox1
                self.hoyre.configure(state=NORMAL)
                self.venstre.configure(state=DISABLED)

        elif fox1 == 2 and boat1 == 0:
            for x in range(0, 100):
                canvas.move(1, -4, 0)
                root.update()
                time.sleep(0.02)
            self.pig.configure(state=NORMAL)
            self.grain.configure(state=NORMAL)
            self.fox.configure(state=DISABLED)
            self.hoyre.configure(state=NORMAL)
            self.venstre.configure(state=DISABLED)

        elif grain1 == 3:
            for x in range(0, 100):
                canvas.move(1, -4, 0)
                canvas.move(7, -4, 0)
                root.update()
                time.sleep(0.02)
                global grain1
                grain1 = 1
                print grain1
                self.venstre.configure(state=NORMAL)
                self.hoyre.configure(state=DISABLED)

        elif grain1 == 2 and boat1 == 0:
            for x in range(0, 100):
                canvas.move(1, -7, 0)
                root.update()
                time.sleep(0.02)
            self.pig.configure(state=NORMAL)
            self.fox.configure(state=NORMAL)
            self.grain1.configure(state=DISABLED)
            self.hoyre.configure(state=NORMAL)
            self.venstre.configure(state=DISABLED)
        elif pig1 == 3:
            for x in range(0, 100):
                canvas.move(1, -4, 0)
                canvas.move(6, -4, 0)
                root.update()
                time.sleep(0.02)
                global pig1
                pig1 = 1
                print pig1
                self.venstre.configure(state=NORMAL)
                self.hoyre.configure(state=DISABLED)
        elif pig1 == 2 and boat1 == 0:
            for x in range(0, 100):
                canvas.move(1, -4, 0)
                root.update()
                time.sleep(0.02)
            self.fox.configure(state=NORMAL)
            self.grain.configure(state=NORMAL)
            self.pig.configure(state=DISABLED)
            self.hoyre.configure(state=NORMAL)
            self.venstre.configure(state=DISABLED)
        else:
            for x in range(0, 100):
                 canvas.move(1, -4, 0)
                 root.update()
                 time.sleep(0.02)
                 self.venstre.configure(state=DISABLED)
                 self.hoyre.configure(state=NORMAL)
#================================================================
    def fox(self):
        if fox1 == 0 and boat1 ==0:
            for x in range(0, 10):
                canvas.move(5, 10, 0)
                root.update()
                time.sleep(0.02)
                self.pig.configure(state=DISABLED)
                self.grain.configure(state=DISABLED)
            global pig1
            fox1 = 1
            print fox1
        elif fox1 == 1 and boat1 ==0:
                for x in range(0, 10):
                    canvas.move(5, -10, 0)
                    root.update()
                    time.sleep(0.02)
                    self.pig.configure(state=NORMAL)
                    self.grain.configure(state=NORMAL)
                    global fox1
                    fox1 = 0
                    print pig1
        elif boat1 == 1 and fox1 ==1:
            global fox1
            fox1 = 2
            print fox1
            for x in range(0, 10):
                canvas.move(5, 10, 0)
                root.update()
                time.sleep(0.02)
                self.pig.configure(state=DISABLED)
                self.grain.configure(state=DISABLED)
        elif boat1 == 1 and fox1 == 2:
            for x in range(0, 10):
                canvas.move(5, -10, 0)
                root.update()
                time.sleep(0.02)
                self.pig.configure(state=DISABLED)
                self.grain.configure(state=DISABLED)
            global fox1
            fox1 = 3
            print fox1
        elif boat1 == 1 and fox1 == 3:
            for x in range(0, 10):
                canvas.move(5, 10, 0)
                root.update()
                time.sleep(0.02)
            global fox1
            fox1 = 2
            print fox1
        elif fox1 == 2 and boat1 == 0:
            print "Ugyldig valg"
            self.pig.configure(state=NORMAL)
            self.grain.configure(state=NORMAL)
        elif fox1 == 2 and boat1 == 1:
            self.fox.configure(state=NORMAL)
#================================================================
    def grain(self):
        if grain1 == 0 and boat1 ==0:
            for x in range(0, 10):
                canvas.move(7, 10, 0)
                root.update()
                time.sleep(0.02)
                self.pig.configure(state=DISABLED)
                self.fox.configure(state=DISABLED)
            global grain1
            grain1 = 1
            print grain1
        elif grain1 == 1 and boat1 ==0:
                for x in range(0, 10):
                    canvas.move(7, -10, 0)
                    root.update()
                    time.sleep(0.02)
                    self.pig.configure(state=NORMAL)
                    self.fox.configure(state=NORMAL)
                    global grain1
                    grain1 = 0
                    print grain1
        elif boat1 == 1 and grain1 ==1:
            global grain1
            grain1 = 2
            print grain1
            for x in range(0, 10):
                canvas.move(7, 10, 0)
                root.update()
                time.sleep(0.02)
                self.pig.configure(state=DISABLED)
                self.fox.configure(state=DISABLED)

        elif boat1 == 1 and grain1 == 2:
            for x in range(0, 10):
                canvas.move(7, -10, 0)
                root.update()
                time.sleep(0.02)
                self.pig.configure(state=DISABLED)
                self.fox.configure(state=DISABLED)
            global grain1
            grain1 = 3
            print grain1
        elif boat1 == 1 and grain1 == 3:
            for x in range(0, 10):
                canvas.move(7, 10, 0)
                root.update()
                time.sleep(0.02)
            global grain1
            grain1 = 2
            print grain1

        elif grain1 ==2 and fox1 == 2:
            self.fox.configure(state=NORMAL)

        elif grain1 == 2 and boat1 == 0:
            print "Ugyldig valg"
            self.pig.configure(state=NORMAL)
            self.fox.configure(state=NORMAL)
#================================================================
    def pig(self):
        if pig1 == 0 and boat1 ==0:
            for x in range(0, 10):
                canvas.move(6, 10, 0)
                root.update()
                time.sleep(0.02)
                self.fox.configure(state=DISABLED)
                self.grain.configure(state=DISABLED)
            global pig1
            pig1 = 1
            print pig1
        elif pig1 == 1 and boat1 ==0:
                for x in range(0, 10):
                    canvas.move(6, -10, 0)
                    root.update()
                    time.sleep(0.02)
                    self.fox.configure(state=NORMAL)
                    self.grain.configure(state=NORMAL)
                    global pig1
                    pig1 = 0
                    print pig1
        elif boat1 == 1 and pig1 ==1:
            global pig1
            pig1 = 2
            print pig1
            for x in range(0, 10):
                canvas.move(6, 10, 0)
                root.update()
                time.sleep(0.02)
                self.fox.configure(state=DISABLED)
                self.grain.configure(state=DISABLED)
        elif boat1 == 1 and pig1 == 2:
            for x in range(0, 10):
                canvas.move(6, -10, 0)
                root.update()
                time.sleep(0.02)
                self.fox.configure(state=DISABLED)
                self.grain.configure(state=DISABLED)
            global pig1
            pig1 = 3
            print pig1
        elif boat1 == 1 and pig1 == 3:
            for x in range(0, 10):
                canvas.move(6, 10, 0)
                root.update()
                time.sleep(0.02)
            global pig1
            pig1 = 2
            print pig1

        elif pig1 == 2 and boat1 == 0:
            print "Ugyldig valg"
            self.grain.configure(state=NORMAL)
            self.fox.configure(state=NORMAL)

#==================================================================
    def hoyre(self):
        global boat1
        boat1 = 1
        print boat1
        if fox1 == 1:
           for x in range(0, 100):
                canvas.move(1, 4, 0)
                canvas.move(5, 4, 0)
                root.update()
                time.sleep(0.02)
                self.venstre.configure(state=NORMAL)
                self.hoyre.configure(state=DISABLED)
        elif grain1 == 1:
            for x in range(0, 100):
                canvas.move(1, 4, 0)
                canvas.move(7, 4, 0)
                root.update()
                time.sleep(0.02)
                self.venstre.configure(state=NORMAL)
                self.hoyre.configure(state=DISABLED)
        elif pig1 == 1:
            for x in range(0, 100):
                canvas.move(1, 4, 0)
                canvas.move(6, 4, 0)
                root.update()
                time.sleep(0.02)
                self.venstre.configure(state=NORMAL)
                self.hoyre.configure(state=DISABLED)
        else:
            for x in range(0, 100):
                 canvas.move(1, 4, 0)
                 root.update()
                 time.sleep(0.02)
                 self.venstre.configure(state=NORMAL)
                 self.hoyre.configure(state=DISABLED)
#================================================================
app = App(root)

root.mainloop()
root.destroy() # optional; see description below
