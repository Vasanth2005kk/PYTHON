import math

ab=int(input("enter the AB:"))
bc=int(input("enter the BC:"))
mc=math.atan2(ab,bc)
mbc=round(math.degrees(mc))
print(mbc,chr(176),sep="")

'''#find angle MBC
import math
ab=10#int(input("enter the ab:"))
bc=10#int(input("enter the bc:"))
ac=math.sqrt(math.pow(ab,2)+math.pow(bc,2))
#print(ac)
mc=ac/2
mbc=math.degrees(mc)
print(mbc)
from math import degrees, atan2

AB = float(input())
BC = float(input())

MBC = round(degrees(atan2(AB, BC)))
print((str(MBC)), chr(176), sep='')
print(chr(176))'''