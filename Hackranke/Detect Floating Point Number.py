n=int(input())
output=[]
for i in range(n):
    input_string=input()
    try:
        if input_string=="0":
            output.append(False)
        elif float(input_string):
            output.append(True)
    except Exception :
        output.append(False)

for j in output:
    print(j)