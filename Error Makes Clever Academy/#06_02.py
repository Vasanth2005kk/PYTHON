'''get input for score out of 100.

If score is < 35="Poor Student"

if score is greater than 35 but < than 70 ="Average Student"

if score is greater than 70="Good Student"'''

score=int(input("enter the mark:"))
if score<35:
    print("poor student")
elif score>=35 and score<70:
    print("average student")
elif score>=70 and score<=100:
    print("good student")
else:
    print("invelid score")
