import cmath
com=complex(input("enter the complex:"))
print(abs(complex(com)))
print(cmath.phase(complex(com)))

'''import math
import cmath
com1=input("enter the complex number:").split("+")
#print(com1)
list_1=[]
list_1.extend(com1[1])
list_1.remove("j")
r_num=list_1[0]
#print(type(int(r_num)))
a=com1[0]
A=int(a)
#print(type(A))
B=int(r_num)
r=math.sqrt(math.pow(A,2)+math.pow(B,2))
print(r)
print(cmath.phase(complex(A,B)))'''
