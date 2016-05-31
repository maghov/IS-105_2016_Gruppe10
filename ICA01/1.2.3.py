# -*- coding: utf-8 -*-

def code():
    '''
    Implementerer en kode: ASCII mapping fra binær string til ASCII string,
    og tilbake. Laster opp tabeller i minnet
    '''
    
    binary = {}
    ascii = {}
    
    # Genererer Ascii kode
    for i in range(0,128) :
        ascii[format(i,'08b')] = chr(i)
    
    
    # Reverserer ascii koden til binært
    for k, v in ascii.iteritems():
        binary[v] = binary.get(v, [])
        binary[v].append(k)   
    
    return ascii # En foreslått vei for å laste opp i minnet

def encode():
    pass

def decode(sourcecode,n, ascii):
    '''
    Dekoderer en kildekode ved bruk av chuncks av størrelse n
    '''
    # Her trengs en ordbok som har mappingen mellom binær string og ASCII karakterer
    
    sentence = ""    
    
    f = open(sourcecode, mode='rb') # Åpner en fil med filnavn <sourcecode>
    while True:
        chunk = f.read(n)           # Leser n antall karakterer fra en åpen fil
        if chunk == '':             # Dette er en måte å sjekke End Of File i Python
            break
        if chunk != '\n':
            
            setence = ""            # ASCII setningen generert
            
            # Lager en setning
            sentence = sentence + ascii[chunk]
            
    return sentence

def test():
    '''  
     En plassholder for noen testtilfeller.
    '''
    
    print decode('filnavn', 8, code())

test()