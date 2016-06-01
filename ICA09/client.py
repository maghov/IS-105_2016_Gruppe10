# Kode er hentet fra:
# http://www.binarytides.com/programming-udp-sockets-in-python
# Koden er tilvirket noe i forhold til ICA

import socket
import sys

# sette opp klienten
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = '10.224.208.74';
port = 8888;

while(1) :
    msg = raw_input('Enter message to send : ')

    try :
        #setter til String
        s.sendto(msg, (host, port))

        # motta data fra klient (data, addr) samt svar
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print 'Server reply : ' + reply

    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
