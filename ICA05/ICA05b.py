def search_fast(haystack, needle): 
    for item in haystack:
        if item == needle: 
            return True
        return False


def search_slow(haystack, needle): 
    return_value = False
    for item in haystack:
        if item == needle: 
            return_value = True
    return return_value

#Liste
haystack = ['def-456', 'ghi-789', 'abc-123', 'jwjdkoa', 'jiwdjwoa', 'j9wadwaa', 'j9qid9']

#Det man soker etter
needle = 'def-456'

#Starter sok
import timeit
print(timeit.timeit("search_fast(haystack, needle)", setup="from __main__ import search_fast, haystack, needle"))