

message = open("hamlet.txt", "r")

def code():
    '''
    Implements an initial table for LZW algorithm
    '''
    table = {}
    table[1] = 'a'
    table[2] = 'b'
    table[3] = 'c'
    table[4] = 'd'
    table[5] = 'e'
    table[6] = 'f'
    table[7] = 'g'
    table[8] = 'h'
    table[9] = 'i'
    table[10] = 'j'
    table[11] = 'k'
    table[12] = 'l'
    table[13] = 'm'
    table[14] = 'n'
    table[15] = 'o'
    table[16] = 'p'
    table[17] = 'q'
    table[18] = 'r'
    table[19] = 's'
    table[20] = 't'
    table[21] = 'u'
    table[22] = 'v'
    table[23] = 'w'
    table[24] = 'x'
    table[25] = 'y'
    table[26] = 'z'
    table[27] = '.'
    table[28] = ','
    table[29] = ' '
    table[30] = ':'
    table[31] = ';'


    return table

def encode(message):
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
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
    test_message = message
    print encode(test_message)

test()
