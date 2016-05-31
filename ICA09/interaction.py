from sm import *
from river import *
import socket
import sys

#Dictionary and list of possible commands and their explanation
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
