name=input("student name:")
sub_1=int(input("subject 1 :"))
sub_2=int(input("subject 2 :"))
sub_3=int(input("subject 3 :"))
sub_4=int(input("subject 4 :"))
sub_5=int(input("subject 5 :"))

total=sub_1+sub_2+sub_3+sub_4+sub_5
pracentage=total/5

print("student name:",name)
print("Total mark:",total)
print(f"pracentage: {int(pracentage)}%")