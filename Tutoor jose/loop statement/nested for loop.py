''' nested for loop statement:
*
**
***
****
*****

for i in range(1,1+5):
    print("*"*i)

for i in range(5+1):
    for j in range(i):
        print("*",end="")
    print(" ")'''

''' 
*****
****
***
**
*

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")'''

'''
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
a-z => 97-112
A-B => 65-90
'''
for i in range(65,70):
    for j in range(65,70):
        print(chr(j),end="")
    print("")