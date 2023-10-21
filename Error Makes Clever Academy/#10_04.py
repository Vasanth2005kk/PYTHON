'''write a program to display the cube of the number up to an integer.
test data
input number of terms: 5
exputed output:
number is: 1 and cube of the 1 is :1
number is: 2 and cube of the 2 is :8
number is: 3 and cube of the 3 is :27
number is: 4 and cube of the 4 is :64
number is: 5 and cube of the 5 is :125
'''
number=int(input("number:"))
for i in range(1,number+1):
    print("Number is :",i,"and cube of the ",i,"is:",i*i*i)
