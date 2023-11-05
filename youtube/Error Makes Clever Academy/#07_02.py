'''. get input for five subjects marks.
Add all of it, And find average.
If average mark is less than 35.
Print "Additional class is required"
else Print "you are good to go"'''

sub1=int(input("enter the subjict_1:"))
sub2=int(input("enter the subjict_2:"))
sub3=int(input("enter the subjict_3:"))
sub4=int(input("enter the subjict_4:"))
sub5=int(input("enter the subjict_5:"))
total=sub1+sub2+sub3+sub4+sub5
print("total=",total)
average=total/5
print("average=",average)
if average<35:
    print("Additional class is required.")
else:
    print("you are good to go.")
