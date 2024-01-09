
import numpy

def arrays(arr):
     b = numpy.array(arr,float)
     return b[::-1]         

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#2
'''
import numpy

print numpy.array(raw_input().split(),float)[::-1]
'''
#3
'''i
mport numpy

print numpy.flipud(numpy.array(raw_input().split(),float))'''