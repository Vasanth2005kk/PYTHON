n=int(input())
set_1=set(input().split(" "))
n1=int(input())
set_2=set(input().split(" "))
c=set_1.intersection(set_2)
print(len(c))