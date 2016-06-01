import shelve
import sys
import os
encoding='UTF-8'

#Oppretter eller åpner filesystem.fs
fs = shelve.open('filesystem.fs', writeback=True)
current_dir = []

def install(fs):

    # Oppretter bruker of root
    username = raw_input('What do you want your username to be? ')

    fs[""] = {"System": {}, "Users": {username: {}}}

#Returnerer filer fra opprettet dictionary
def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    d = fs[""]

    for key in current_dir:
        d = d[key]
    return d

#Viser contents
def ls(args):

    print 'Contents of directory', "/" + "/".join(current_dir) + ':'

    for i in current_dictionary():

        print i

#AApner contents
def cd(args):

    if len(args) != 1:

        print "Usage: cd "
        return

    if args[0] == "..":
        if len(current_dir) == 0:
            print "Cannot go above root"
        else:
            current_dir.pop()
    elif args[0] not in current_dictionary():
        print "Directory " + args[0] + " not found"
    else:
        current_dir.append(args[0])

#Lager directory
def mkdir(args):
    if len(args) != 1:
        print "Usage: mkdir "
        return

#Lager tom dictionary og returnerer til root brukernavn
    d = current_dictionary()[args[0]] = {}
    fs.sync()

#Skriver ut gjeldende directory
def pwd(args):

    d=current_dir
    print d[-1]

#Avslutt - gaa ut av directory
def quit(args):
    sys.exit(0)

#Lager ny fil i selve directory
def add(args):
	full_path = '/'.join(current_dir + ["test.txt"])
	with open(full_path, "a+") as f:
    		f.write("test")
#Sletter directory
def rmdir(args):
	os.rmdir('/'.join(current_dir + ["test"]))

COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir,'pwd':pwd,'quit':quit,'rmdir':rmdir}

install(fs)

while True:
    raw = raw_input('> ')
    cmd = raw.split()[0]
    if cmd in COMMANDS:
        COMMANDS[cmd](raw.split()[1:])

raw_input('Press the Enter key to shutdown...')
