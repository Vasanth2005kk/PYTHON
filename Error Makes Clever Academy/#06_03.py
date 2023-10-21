'''. Make a mini calculator

Get input for 2 numbers a and b

Get input from user whether to add/sub/mul/div

If user selects add then add the two number and Print the result.'''
a=int(input("enter the  A:"))
b=int(input("enter the  b:"))
print("add\nsub\nmul\ndiv")
calculator=input("enter:")
if calculator=="add":
    print("add=",a+b)
elif calculator=="sub":
    print("sub=",a-b)
elif calculator=="mul":
    print("mul=",a*b)
elif calculator=="div":
    print("div=",a/b)
else:
    print("not this work")
