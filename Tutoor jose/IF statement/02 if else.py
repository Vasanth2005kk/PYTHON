# if else statement

# write a program to check vote eligibility by enter his/her name and age

name=input("enter your name:") 
age=int(input("enter the age:"))
if 18<=age: #age>=18
    print(name,"is eligible for vote")
else:
    print(name,"is not eligible")