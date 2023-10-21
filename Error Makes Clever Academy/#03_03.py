'''get intger input for variablea,b,c.
multiply all 3 variable(a*b*c)
add all variable(a+b+c)
divide the multiplied value by added values
print it
sample input:
2
3
4
sample output:
2.6'''
a=int(input("enter A:"))
b=int(input("enter B:"))
c=int(input("enter C:"))
d=(a*b*c)/(a+b+c)
print('{:.1f}'.format(d))
