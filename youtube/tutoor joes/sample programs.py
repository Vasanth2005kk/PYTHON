marks=input("Enter the marks:").split(",")
output=[]
for i in marks:
    intger=int(i)
    if intger>=35:
        output.append("pass")
    else:
       output.append("fail")
print(output)