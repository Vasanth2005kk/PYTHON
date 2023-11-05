'''get input for a and b and passit to the function called printrange()
let the function print number from a to b'''
def printrange(n1,n2):
    for i in range(n1+1,n2):
        print(i)
number_1=int(input("enter the range_1:"))
number_2=int(input("enter the range_2:"))
printrange(number_1,number_2)
