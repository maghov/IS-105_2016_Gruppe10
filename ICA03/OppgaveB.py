from sys import argv 

message = raw_input()
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
    table[6] = 'i'
    table[9] = 'j'
    table[10] = 'k'
    table[11] = 'l'
    table[12] = 'm'
    table[13] = 'n'
    
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
    
print encode(message)

## DECODE 


    
    

    

#def test():
#    test_message = "hei dette er meg"
#    print encode(test_message)
    
#test()
