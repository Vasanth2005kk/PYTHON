'''get a intger number form user and pass it to the function called
findevenodd(). let the function print whether thenumber is even or
odd'''
def findevenodd(number):
    if number%2==0:
        print(number,"is even number.")
    else:
        print(number,"is odd number.")

n=int(input("enter the number:"))
findevenodd(n)
