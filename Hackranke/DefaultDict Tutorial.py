n,m=map(int,input().split())
A=[]
B=[]
for i in range(n):
    a=input()
    A.append(a)

for i in range(m):
    b=input()
    B.append(b)
   
 
for i in B:
    if i in A:
        for j in range(len(A)):
            if i==A[j]:
                print(j+1,end=" ")
        print()
    else:
        print(-1)
