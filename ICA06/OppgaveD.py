# -*- coding: utf-8 -*-

from sm import SM
import Database
class River(SM):

<<<<<<< HEAD:ICA06/OppgaveD

=======
<<<<<<< HEAD
    river_db = []
=======
    
>>>>>>> 972072b89b342385e0a3c1e4d731ff321b95d5ab
>>>>>>> c8ee5140f3b44658358c6248e62be8c1bfb5ce23:ICA06/OppgaveD.py

    # Blir kalt hver gang klassen blir instansiert
    def __init__(self, initialValue):
        self.startState = initialValue
        self.river_db = self.startState
##############################################################################
    def crossriver(self):#Holder styr på om båten er på høyre eller venstre side
        # Båten er til høyre
        if ['boat isat left'] in self.river_db:
            self.remove(['boat isat left'])
            self.add(['boat isat right'])
        # Båten er til venstre
        elif ['boat isat right'] in self.river_db:
            self.remove(['boat isat right'])
            self.add(['boat isat left'])

        #CHICKEN# Båten er til venstre og kyliing er i båten
        elif ['boat isat left 'and' chicken in boat'] in self.river_db:
            self.remove(['boat isat left'])
            self.remove(['chicken isat left'])
            self.add(['boat isat right'])
            self.add(['chicken isat boat'])
        # Båten er til høyre og kylling er i båten
        elif ['boat isat right 'and' chicken in boat'] in self.river_db:
            self.remove(['boat isat right'])
            self.add(['boat isat right'])

        #GRAIN# Båten er til venstre og korn er i båten
        elif ['boat isat left 'and' grain in boat'] in self.river_db:
            self.remove(['boat isat left'])
            self.remove(['grain isat left'])
            self.add(['boat isat right'])
            self.add(['grain isat boat'])
        # Båten er til venstre og korn er i båten
        elif ['boat isat right' and 'grain in boat'] in self.river_db:
            self.remove(['boat isat right'])
            self.remove(['grain isat right'])
            self.add(['boat isat right'])
            self.add(['grain isat boat'])

        #PIG# Båten er til venstre og grisen er i båten
        elif ['boat isat right' and 'pig in boat'] in self.river_db:
            self.remove(['boat isat right'])
            self.remove(['pig isat right'])
            self.add(['boat isat right'])
            self.add(['pig isat boat'])
        # Båten er til venstre og grisen er i båten
        elif ['boat isat right' and 'pig in boat'] in self.river_db:
            self.remove(['boat isat right'])
            self.remove(['pig isat right'])
            self.add(['boat isat right'])
            self.add(['pig isat boat'])
###############################################################################
    def putin(self, item):
        #chicken
        if ['boat isat left' and 'chicken isat left'] in self.river_db:
            self.remove(['chicken isat left'])
            self.add(['chicken in boat'])
        elif ['boat isat left' and 'chicken in boat'] in self.river_db:
            self.remove(['chicken in boat'])
            self.add(['chicken isat left'])
        elif ['boat isat right' and 'chicken in boat'] in self.river_db:
            self.remove(['chicken in boat'])
            self.add(['chicken isat right'])
        elif ['boat isat right' and 'chicken isat right'] in self.river_db:
            self.remove(['chicken isat right'])
            self.add(['chicken in boat'])
            #fox
        elif ['boat isat left' and 'fox isat left'] in self.river_db:
            self.remove(['fox isat left'])
            self.add(['fox in boat'])
        elif ['boat isat left' and 'fox in boat'] in self.river_db:
            self.remove(['fox in boat'])
            self.add(['fox isat left'])
        elif ['boat isat right' and 'fox in boat'] in self.river_db:
            self.remove(['fox in boat'])
            self.add(['fox isat right'])
        elif ['boat isat right' and 'fox isat right'] in self.river_db:
            self.remove(['fox isat right'])
            self.add(['fox in boat'])
        #grain
        elif ['boat isat left' and 'grain isat left'] in self.river_db:
            self.remove(['grain isat left'])
            self.add(['grain in boat'])
        elif ['boat isat left' and 'grain in boat'] in self.river_db:
            self.remove(['grain in boat'])
            self.add(['grain isat left'])
        elif ['boat isat right' and 'grain in boat'] in self.river_db:
            self.remove(['grain in boat'])
            self.add(['grain isat right'])
        elif ['boat isat right' and 'grain isat right'] in self.river_db:
            self.remove(['grain isat right'])
            self.add(['grain in boat'])


    # Osv., - definer alle kommandoen som virker på "verden" her ...

    def view(self):
        # Her implementeres logikken for "vakker" utskrift
        # ...
        print "** Here is the state of the river-world:"

        allAtLeft       = "** [chicken fox grain man ---\\ \\_ _/ ________________ /---]"
        allAtLeftCInB   = "** [fox grain man ---\\ \\_ chicken _/ ________________ /---]"
        BoatAtRightCAtR = "** [ fox grain man ---\\ _________________\\_ _/ /--- chicken]"
        BoatAtLeft 		= "** [ fox grain man ---\\ \\__/ ________________ /--- chicken]"
        BoatAtRightCM 	= "** [ grain man ---\\ \\fox / ________________ /--- chicken]"



        # .... slik kan alle tilstander "tegnes"


        # Bruk betingelse og finn ut tilstanden fra database (db, som er en liste av lister)
        # For eksempel, hvis alt er på venstre siden av elven, skriv ut allAtLeft "bilde"
        # Dette er ikke en korrekt kode, - man bør sjekke på flere tilstandsvariabler
        # eller implementere datastrukturer som genererer "bilder" automatisk, basert på innholdet
        # i databasen
        if ['boat isat left'] in self.river_db:
            print allAtLeft
        elif ['boat isat right'] in self.river_db:
            print onlyBoatAtRight
        else:
            print ";;; MISHAP - SOMETHING WENT WRONG!"

    # Denne funksjonen skal definere alle overgangene fra en tilstand til en annen
    # De kan være mange, så her må man skrive en smart kode
    # Eksperimentere først med enkelte kommandoer, og så implementere denne funksjonen
    def getNextValues(self, state, inp):
        # input her er et kommandonavn og den tilsvarende funksjonen må kalles opp
        pass

    # Database "saker", bør ligge i egen modul
    def database(self):
        print self.river_db
    def add(self, item):
        self.river_db.append(item)
    def remove(self, item):
        self.river_db.remove(item) # typisk MISHAP, hvis item ikke finnes i listen river_db


# Test cases
r = River([['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'], ['grain isat left']])
r.start()
r.database() # Data representasjon av verden til enhver tid
r.view()
r.crossriver() # Dette skulle ikke være mulig, men foreløpig ingen "constraints" er definert!
r.database()
r.view()
r.crossriver() # Dette skal ikke kunne gå heller ...
r.view()