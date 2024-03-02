#prime number or not

output=[]

num=7
for i in range(2,num):
    if num%i == 0:
        output.append(i)

if not output :
    print("prime number :",num)
else:
    print("not prime number :",num)