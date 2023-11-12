m=int(input())
m1=set(map(int,input().split(" ")))
n=int(input())
n1=set(map(int,input().split(" ")))
c=m1.symmetric_difference(n1)
c1=list(c)
c1.sort()
for i in c1:
    print(i)