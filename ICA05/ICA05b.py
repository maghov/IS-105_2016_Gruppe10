import timeit
 
  
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
    
    
def test_slow(): 
	int = range(1000000) 
	search_slow(int, 900000)
	
	
	"""liste = []
	for i in range(500):
		liste.append(i)
		chr(i)"""
	
	
def test_fast(): 
	int = range(1000000)
	search_fast(int, 900000)
	
	 
print(timeit.timeit("test_slow()", setup="from __main__ import test_slow", number = 10))
print(timeit.timeit("test_fast()", setup="from __main__ import test_fast", number = 10))
