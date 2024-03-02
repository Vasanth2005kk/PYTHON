output=[]

while True:
    goles=input("Enter the your goles:")
    if goles:
        output.append(goles)
    else:
        break
output.sort()
for i in output:
    print(i)