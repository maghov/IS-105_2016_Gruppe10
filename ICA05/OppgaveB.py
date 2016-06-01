import timeit # impoterer timeit
# -*- coding: utf-8 -*-

def search_fast(haystack, needle): # motode for å søke gjennom haystack
    for item in haystack:          # for element i haystack
        if item == needle:         # hvis item = needle
        	return True            # Return sant
    return False                   # hvis ikke sant, return false.


def search_slow(haystack, needle): # "slow" metode for å søke
    return_value = False           #
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value


def test_slow():
	int = range(1000000)           # Haystack på 1 million
	search_slow(int, 900000)       # Needle på 900k



def test_fast():
	int = range(1000000)          # Haystavk på 1 million
	search_fast(int, 900000)      # Needle på 900k

# print metode som også bruke timeit, for å kjøre søkemetodene 10 ganger.
print(timeit.timeit("test_slow()", setup="from __main__ import test_slow", number = 10))
print(timeit.timeit("test_fast()", setup="from __main__ import test_fast", number = 10))
