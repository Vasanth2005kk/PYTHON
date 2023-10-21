x=int(input("Enter the X:"))
y=int(input("Enter the Y:"))
z=int(input("Enter the Z:"))
n=int(input("Enter the N:"))
list_1=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k !=n:
                list_1.append([i,j,k])
print(list_1)
