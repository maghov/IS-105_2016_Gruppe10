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
    if data == "Start":
        #Starter funksjonen testStart
        testStart()
        break
        #Tester hvis data fra clienten stemmer med "Chicken"
        if data =='Chicken':
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
