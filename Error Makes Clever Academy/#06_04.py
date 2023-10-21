'''7.Get a input for score percentage.
Only If the percentage is greater than 70,
get input for his name, department and location.
Then print you are elgibile.
If not print you are not eligible.'''
age=int(input("enter the age:"))
if age>70:
    name=input("enter the name:")
    department=input("enter the department")
    location=input("enter the location")
    print("your eligible")
else:
    print("not eligible")
