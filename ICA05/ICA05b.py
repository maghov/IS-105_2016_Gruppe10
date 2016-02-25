import timeit

haystack = open('test.txt', 'r+').read()
needle = ''

def search_fast(haystack, needle):
    for item in haystack:
        return True
    return False


def search_slow(haystack, needle): 
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value



search_slow(haystack, needle)
print(timeit.timeit("search_slow(haystack, needle)", setup="from __main__ import search_slow, haystack, needle"))

search_fast(haystack, needle)
print(timeit.timeit("search_fast(haystack, needle)", setup="from __main__ import search_fast, haystack, needle"))