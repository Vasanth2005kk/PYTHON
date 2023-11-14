n=int(input())
list_1=[]
for i in range(n):
    S=int(input())
    A=set(map(int,input().split()))
    T=int(input())
    B=set(map(int,input().split()))
    list_1.append(A.issubset(B))
for j in list_1:
    print(j)