n=int(input())
arr=list(map(int,input().split(" ")))

if n==len(arr):
    output=arr[::-1]

for i in output:
    print(i,end=" ")