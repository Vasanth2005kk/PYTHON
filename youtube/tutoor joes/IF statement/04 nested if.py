# Nested if statement
'''
student mark example program
3 make as input:
total
average
result: if pass grade
90-100 =A
80-89  =B
70-79  =C
60-35  =D
'''
m1=int(input("enter mark-1:"))
m2=int(input("enter mark-2:"))
m3=int(input("enter mark-3:"))
total=m1+m2+m3
print("total:",total)
average=total/3.0
print("avreage:",average)
if m1>=35 and m2>=35 and m3>=35:
    print("pass")
    if average>=90 and average<=100:
        print("grade:A")
    elif average>=80 and average<=89:
        print("grade:B")
    elif average>=70 and average<+79:
        print("grade:C")
    else:
        print("grade:D")
else:
    print("fail:")
    print("No grade")