'''Get input for salary and age.
If salary greater than or equal to 20000 or age less than or equal to 25,
get input for required loan amount.
If not print you are not eligible for loan
If required loan amount is less than or equal to 50,000
print You are eligible for loan.
If it is greater than 50,000 print maximum loan amount is 50000.'''

salary=int(input("enter the salary:"))
age=int(input("enter the age:"))
if salary>20000 or age>25:
    print("you are eligible for loan")
    loan=int(input("yor loan amount:"))
    if loan<50000:
              print(" You are eligible for loan.")
    else:
         print("maximum loan amount is 50000.")
else:
    print("you are not eligible for loan")
