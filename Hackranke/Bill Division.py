a=list(map(int,input().split()))
b=list(map(int,input().split()))
subration_value=int(input())

b.remove(b[a[1]])

count=0
for i in b:
    count+=i
output=subration_value-(count//2)
if output==0:
    print("Bon Appetit")
else:
    print(output)