'''(a+b)*c
get input for a and b function called add() which should return the sum of a and b
and multiply that sum with c '''
a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))
def add():
    return a+b
print(add()*c)
