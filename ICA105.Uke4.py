import sys
 
# define file pointers and bytelength
file_in = open("sourcecode.txt")
file_out = open("sourcecode_out.txt","wb")
bl = 8
 
# read input file; remove whitespaces
# make list of bits (ints) from input
bitlist = map(int,''.join(file_in.read().split()))
if len(bitlist)%bl != 0:
    sys.exit("length of bitlist not integer multiple of %s" % bl)
 
# assemble resultstring:
# - make list of bytes from `bitlist`
# - evaluate each byte -> int -> ascii char
rs = ''.join([chr(sum(bit<<abs(idx-bl)-1 for idx,bit in enumerate(y)))
               for y in zip(*[bitlist[x::bl] for x in range(bl)])
              ])
 
# write output
file_out.write(rs)
file_out.close()
