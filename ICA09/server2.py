# -*- coding: utf-8 -*-
# Kode for kommunikasjon over nettverk er hentet fra.
# http://www.binarytides.com/programming-udp-sockets-in-python

import socket
import sys
from sm import SM


class River(SM):

    river_db = [] # En klønete måte å definere database på, bør være i egen klasse og kanskje ikke en liste?

    # Blir kalt hver gang klassen starter
    def __init__(self, initialValue):
        self.startState = initialValue
        self.river_db = self.startState


    def crossriver(self):
        #Funksjoner for å krysse elva
            #Båt høyre
            if ['boat isat left'] in self.river_db:
                self.remove(['boat isat left'])
                self.add(['boat isat right'])
                self.updateWorld()
            #Båten venstre
            elif ['boat isat right'] in self.river_db:
                self.remove(['boat isat right'])
                self.add(['boat isat left'])
                self.updateWorld()
            #KYLLING
            #Båten er til venstre og kyliing er i båten
            elif ['boat isat left 'and' chicken isat boat'] in self.river_db:
                    self.remove(['boat isat left'])
                    self.remove(['chicken isat left'])
                    self.add(['boat isat right'])
                    self.add(['chicken isat boat'])
                    self.updateWorld()
            #Båten er til høyre og kylling er i båten
            elif ['boat isat right 'and' chicken isat boat'] in self.river_db:
                    self.remove(['boat isat right'])
                    self.add(['boat isat right'])
                    self.updateWorld()
            #GRAIN
            #Båten er til venstre og grain er i båten
            elif ['boat isat left 'and' grain isat boat'] in self.river_db:
                    self.remove(['boat isat left'])
                    self.remove(['grain isat left'])
                    self.add(['boat isat right'])
                    self.add(['grain isat boat'])
                    self.updateWorld()
            #Båten er til venstre og grain er i båten
            elif ['boat isat right' and 'grain isat boat'] in self.river_db:
                    self.remove(['boat isat right'])
                    self.remove(['grain isat right'])
                    self.add(['boat isat right'])
                    self.add(['grain isat boat'])
                    self.updateWorld()
            #FOX
            #Båten er til venstre og fox er i båten
            elif ['boat isat right' and 'fox isat boat'] in self.river_db:
                    self.remove(['boat isat right'])
                    self.remove(['fox isat right'])
                    self.add(['boat isat right'])
                    self.add(['fox isat boat'])
                    self.updateWorld()
            # Båten er til venstre og pig er i båten
            elif ['boat isat right' and 'pig isat boat'] in self.river_db:
                    self.remove(['boat isat right'])
                    self.remove(['pig isat right'])
                    self.add(['boat isat right'])
                    self.add(['pig isat boat'])
                    self.updateWorld()

    #Setter inn item i båt.
    def putIn(self, item):
        if ([item +' isat left'] in self.river_db):
            self.remove([item+' isat left'])
        else:
            self.remove([item+' isat right'])
        self.add([item+' isat boat'])
        self.updateWorld()

    #Tar ut item fra båt.
    def takeOut(self, item):
        self.remove([item+' isat boat'])
        if ['boat isat left'] in self.river_db:
            self.add([item+' isat left'])
        if ['boat isat right'] in self.river_db:
            self.add([item+' isat right'])
        self.updateWorld()


    def interface(self):
        # Vakker utskrift
        print "** Here is the state of the river-world:"

        self.s1         = "** [chicken fox grain ---\\ \\__/ _____________/---]"
        self.s2         = "** [fox grain ---\\ \\_chicken_/ _____________/---]"
        self.s3         = "** [fox grain---\\ \ _________________\_ chicken_//---]"
        self.s4         = "** [fox grain---\\ \ _________________\__//---chicken]"
        self.s5         = "** [fox grain---\\ \ _________________\__//---chicken]"
        self.s6         = "** [fox grain---\\ \\__/ ________________ /---chicken]"
        self.s7         = "** [fox grain---\\ \\__/ ________________ /---chicken]"
        self.s8         = "** [fox ---\\ \\_grain_/ ________________ /---chicken]"
        self.s9         = "** [fox ---\\ \________________ \_grain_/ /---chicken]"
        self.s10        = "** [fox---\\ \________________ \__/ /---grain chicken]"
        self.s11        = "** [fox---\\ \________________ \__/ /---grain chicken]"
        self.s12        = "** [fox---\\ \________________ \_chicken_/ /---grain ]"
        self.s13        = "** [fox ---\\ \\_chicken_/ ________________ /---grain]"
        self.s14        = "** [fox chicken---\\ \\__/ ________________ /---grain]"
        self.s15        = "** [fox chicken---\\ \\__/ ________________ /---grain]"
        self.s16        = "** [chicken---\\ \\_fox_/ ________________ /---grain]"
        self.s17        = "** [chicken---\\ \________________ \_fox_/ /---grain ]"
        self.s18        = "** [chicken---\\ \________________ \__/ /---fox grain ]"
        self.s19        = "** [chicken---\\ \________________ \__/ /---fox grain ]"
        self.s20        = "** [chicken---\\ \\__/ ________________ /---fox grain]"
        self.s21        = "** [chicken---\\ \\__/ ________________ /---fox grain]"
        self.s22        = "** [---\\ \\_chicken_/ ________________ /---fox grain]"
        self.s23        = "** [---\\ \________________ \_chicken_/ /---fox grain ]"
        self.s24        =  "** [---\\ \________________ \__/ /---chicken fox grain ]"
        self.s25        = "Congratulations! The farmer can now sell his goods at the market!"
        #Tilstander der spillet avsluttes
        self.s26         = "** [chicken fox ---\\ \\_grain_/ _____________/---]"
        self.s27         = "** [chicken fox ---\\ \ _____________\_grain_//---]"
        self.s28         = "** [chicken grain ---\\ \\_fox_/ _____________/---]"
        self.s29         = "** [chicken grain ---\\ \ _____________\_fox_//---]"
        self.allAtRight      = "** [---\\ \\__/ ________________ /---chicken fox grain]"


        # Finner tilstanden fra database og printer utskriften som passer med tilstanden.

    def statusCheck(self):

        #Alle venstre
        if ['boat isat left'] in self.river_db and ['fox isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s1

        #Alle venstre, kylling i båt.
        elif ['boat isat left'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s2

        # Alle venstre, kylling i båt høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s3

        # Alle venstre, kylling høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s4

        # Båt venstre, kylling høyre, resten venstre
        elif ['boat isat left'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s6

        # Båt venstre, kylling høyre, fox venstre, grain i båt
        elif ['boat isat left'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.s8

        #Båt høyre, kylling høyre, fox venstre, grain i båt
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.s9

        #Båt høyre, kylling høyre, fox venstre, grain høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s10

        #Båt høyre, kylling i båt, fox venstre, grain høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s12

        #Båt venstre, kylling i båt, fox venstre, grain høyre
        elif ['boat isat left'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s13

        #Båt venstre, kylling venstre, fox venstre, grain høyre
        elif ['boat isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s14

        #Båt venstre, kylling venstre, fox i båt, grain høyre
        elif ['boat isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat boat'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s16

        #Båt høyre, kylling venstre, fox i båt, grain høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat boat'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s17

        #Båt høyre, kylling venstre, fox høyre, grain høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s18

        #Båt venstre, kylling venstre, fox venstre, grain høyre
        elif ['boat isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s20

        #Båt venstre, kylling i båt, fox høyre, grain høyre
        elif ['boat isat left'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s22

        #Båt høyre, kylling i båt, fox høyre, grain høyre
        elif ['boat isat right'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s23

        #Båt høyre, kylling i høyre, fox høyre, grain høyre #WIN
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s24
        #Printer at du har vunnet.
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s25

        #Båt venstre, fox venstre, kylling høyre, grain i båt
        elif ['boat isat left'] in self.river_db and ['fox isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.s26

        #Båt høyre, fox venstre, kylling venstre #TAP
        elif ['boat isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.s27

        #Båt venstre, fox i båt, kylling venstre, grain venstre
        elif ['boat isat left'] in self.river_db and ['fox isat boat'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s28

        #Båt høyre, fox i båt, kylling venstre, grain venstre #TAP
        elif ['boat isat right'] in self.river_db and ['fox isat boat'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s29


    def winCondition(self):
        #Sjekker om du har tapt og avslutter verden hvis dette stemmer
        if ['boat isat right'] in self.river_db:
            if ['chicken isat left'] in self.river_db and ['grain isat left'] in self.river_db:
                print 'MISHAP -- The chicken has eaten the grain! Try again.'
                self.killWorld()
            elif ['chicken isat left'] in self.river_db and ['fox isat left'] in self.river_db:
                print 'MISHAP -- The fox has eaten the chicken! Try again.'
                self.killWorld()

        #Sjekker om du har tapt og avslutter verden hvis dette stemmer
        if ['boat isat left'] in self.river_db:
            if ['chicken isat right'] in self.river_db and ['grain isat right'] in self.river_db:
                print 'MISHAP -- The chicken has eaten the grain! Try again.'
                self.killWorld()
            elif ['chicken isat right'] in self.river_db and ['fox isat right'] in self.river_db:
                print 'MISHAP -- The fox has eaten the chicken! Try again.'
                self.killWorld()

        #Sjekker om du har vunnet
        elif ['chicken isat right'] in self.river_db and ['grain isat right'] in self.river_db and ['fox isat right'] in self.river_db:
            print self.s25
            self.killWorld()

    # Database
    def database(self):
        print self.river_db
    def add(self, item):
        self.river_db.append(item) #Legger til objekt i databasen
    def remove(self, item):
        self.river_db.remove(item) # Fjerner objekt fra databasen
    def updateWorld(self): # Oppdaterer verden og sjekker at alt er i orden
        self.interface()
        self.statusCheck()
        self.winCondition()

    #Avslutter verden
    def killWorld(self):
        sys.exit()



# Kode er hentet fra:
# http://www.binarytides.com/programming-udp-sockets-in-python
# Koden er tilvirket noe i forhold til ICA

import socket
import sys

HOST = 'localhost'   # IP til server som clienten kobler til
PORT = 8888 # Port til HOST

# Oppretter en socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


#  - Setter opp og binder forbindelsen
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Jobber med klienter og mottar data
while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    #Tester hvis data fra clienten stemmer med "Start"
    if (data == "Start"):
        #Starter funksjonen testStart
        testStart()
        break
        #Tester hvis data fra clienten stemmer med "Chicken"
        if (data =='Chicken'):
            reply = 'LOL'
            s.sendto(reply , addr)
            print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    else:
        reply = 'Feil svar, proev igjen!'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

    #Funksjon som importerer river crossing spillet.
    def testStart():
        reply = 'Starter spill'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
        import runme
        return

#Lukker forbindelsen
s.close()




commandexplaination = {'chicken' : 'cross with chicken', 'fox' : 'cross with a fox', 'grain' : 'cross with grain', 'none' : 'cross without any items', 'quit' : 'ends the simulation', 'restart' : 'restarter programmet'}
possiblecommands = ['chicken', 'fox', 'grain', 'none', 'quit', 'solvePuzzle', 'db', 'restart']

def db():
    r.database()
    fullLoop()

#Function to print the explanation of possible commands to the user.
def help():
    print 'List of possible commands:'
    print 'chicken: '+commandexplaination['chicken']
    print 'fox: '+commandexplaination['fox']
    print 'grain: '+commandexplaination['grain']
    print 'none: '+commandexplaination['none']
    print 'quit: '+commandexplaination['quit']
    print 'restart: '+commandexplaination['restart']
    fullLoop()

def restart():
    self.startState = initialValue
    self.river_db = self.startState

#
def returnInput():
    print '------------------------------------------------------------'
    print 'Which good would you like to move? Press return to step through the simulation. Type help for commands'
    inp = raw_input('')
    return inp


def skipper():
    raw_input('')

def fullCrossItem(good):
    r.putIn(good)
    skipper()
    r.crossriver()
    skipper()
    r.takeOut(good)
    fullLoop()

def fullCrossNoItem():
    skipper()
    r.crossriver()
    skipper()
    skipper()
    fullLoop()

def quickCrossItem(good): # A version that does not require return key inputs to step through the process, nor loops back to command input. Mostly used for testing/solving quickly.
    r.putIn(good)
    r.crossriver()
    r.takeOut(good)

def quickCrossNoItem(): # A version that does not require return key inputs to step through the process, nor loops back to command input. Mostly used for testing/solving quickly.
    r.crossriver()

def solvePuzzle(c, g, f):
    quickCrossItem(c)
    quickCrossNoItem()
    quickCrossItem(g)
    quickCrossItem(c)
    quickCrossItem(f)
    quickCrossNoItem()
    quickCrossItem(c)

def fullLoop():
    temp = returnInput()
    if (temp == 'none'):
        fullCrossNoItem()
    elif (temp == 'help'):
        help()
    elif (temp == 'quit'):
        quit()
    elif (temp not in possiblecommands):
        print '---Invalid command!---'
        help()
    # Quick solution for testing purposes
    elif (temp == 'solvePuzzle'):
        solvePuzzle('chicken', 'grain', 'fox')
    elif (temp == 'db'):
        db()
    else:
        fullCrossItem(temp)



# Start the river simulation, update and show state. Start Main loop
r = River([['boat isat left'],['chicken isat left'],['fox isat left'],['grain isat left']])
r.start()
r.updateWorld()
fullLoop()

# Grab the possibility to end the simulation from river.py
def quit():
    r.killWorld()
