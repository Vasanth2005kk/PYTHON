from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
#print(A)
#print(B)
variable=list(product(A,B))
for i in variable:
    print(i,end=" ")