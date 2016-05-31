import timeit


def search_fast(haystack, needle):
    for item in haystack:                       #Går gjennom alle items i lista
        if item == needle:                      #Sjekker om noen items er lik needle(søkeordet)
        	return True                         #Returnerer true hvis den finner needle i haystacken
    return False                                #Returnerer false hvis ikke


def search_slow(haystack, needle):
    return_value = False                        #Returverdi er lik false
    for item in haystack:                       #Går gjennom items i lista
        if item == needle:                      #Hvis den finner et item lik needle
            return_value = True                 #Blir returverdien true
    return return_value                         #Returnerer returverien


def test_slow():
	int = range(1000000)                       #Antall elementer i lista
	search_slow(int, 900000)                   #Hvor i lista søket avsluttes



def test_fast():
	int = range(1000000)                       #Antall elementer i lista
	search_fast(int, 900000)                   #Hvor i lista søket avsluttes




     #kjører søket x-antall ganger og printer tiden det tar å kjøre gjennom.

print(timeit.timeit("test_slow()", setup="from __main__ import test_slow", number = 10))
print(timeit.timeit("test_fast()", setup="from __main__ import test_fast", number = 10))
