# -*- coding: utf-8 -*-
from sm import *
from river import *
import socket
import sys

#Liste over mulige kommandoer og beskrivelse av hva de gjør.
commandexplaination = {'chicken' : 'cross with chicken', 'fox' : 'cross with a fox', 'grain' : 'cross with grain', 'none' : 'cross without any items', 'quit' : 'ends the simulation', 'restart' : 'restarter programmet'}
possiblecommands = ['chicken', 'fox', 'grain', 'none', 'quit', 'solvePuzzle', 'db', 'restart']

#Printer databasen
def db():
    r.database()
    fullLoop()

#Funksjon som printer mulige kommandoer for brukeren
def help():
    print 'List of possible commands:'
    print 'chicken: '+commandexplaination['chicken']
    print 'fox: '+commandexplaination['fox']
    print 'grain: '+commandexplaination['grain']
    print 'none: '+commandexplaination['none']
    print 'quit: '+commandexplaination['quit']
    print 'restart: '+commandexplaination['restart']
    fullLoop()

#Funksjon for å restarte spillet. Virker ikke helt enda.
def restart():
    self.startState = initialValue
    self.river_db = self.startState

#Printer dette i starten av koden og bruker det du skriver som input.
def returnInput():
    print '------------------------------------------------------------'
    print 'Which good would you like to move? Press return to step through the simulation. Type help for commands'
    inp = raw_input('')
    return inp

#Lager et tomt felt for å skrive inn tekst
def skipper():
    raw_input('')

#Funksjon for å crossriver med et objekt
def fullCrossItem(good):
    r.putIn(good)
    skipper()
    r.crossriver()
    skipper()
    r.takeOut(good)
    fullLoop()

#Funksjon for å krysse uten objekter
def fullCrossNoItem():
    skipper()
    r.crossriver()
    skipper()
    fullLoop()

def quickCrossItem(good): # En funksjon brukt for testing og å løse oppgaven fort.
    r.putIn(good)
    r.crossriver()
    r.takeOut(good)

def quickCrossNoItem(): # En funksjon brukt for testing og å løse oppgaven fort.
    r.crossriver()

#Løser spillet automatisk ved hjelp av testfunksjonene
def solvePuzzle(c, g, f):
    quickCrossItem(c)
    quickCrossNoItem()
    quickCrossItem(g)
    quickCrossItem(c)
    quickCrossItem(f)
    quickCrossNoItem()
    quickCrossItem(c)

#Funksjon som sjekker hva du skriver og gjør handlinger utifra dette
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
    # Kommando for å løse spillet automatisk.
    elif (temp == 'solvePuzzle'):
        solvePuzzle('chicken', 'grain', 'fox')
    elif (temp == 'db'):
        db()
    else:
        fullCrossItem(temp)



# Starter riverspillet
r = River([['boat isat left'],['chicken isat left'],['fox isat left'],['grain isat left']])
r.start()
r.updateWorld()
fullLoop()

# Avslutter spillet
def quit():
    r.killWorld()
