fo = open("hamlet1.txt", "r") #Åpner filen hamlet.


def code():

    #Implementerer en tabel for LZW lgoritime.
    table = {}
    table[1] = 't'
    table[2] = 'o'
    table[3] = 'b'
    table[4] = 'e'
    table[5] = 'r'
    table[6] = 'n'
    table[7] = ' '
    return table




def encode(fo):
    table = code()
    string = ""
    code_for_string = []
    for byte in fo:
        symbol = byte
        if (string + symbol) in table.values():
            string = string + symbol
        else:
            for k,v in table.iteritems():
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string

def test():
	print encode(fo)
test()

#print fo.read()
