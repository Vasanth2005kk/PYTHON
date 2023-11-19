s=set(map(int,input().split(" ")))
n=int(input())
set_1=[]
for _ in range(n):
    a=set(map(int,input().split(" ")))
    set_1.append(a)
#print(set_1)
count=0
list_2=[]
for i in s:
    for j in set_1[count]:
        if i==j:
            list_2.append(j)
#print("list_2:",list_2)
len_s1=len(set_1[count])
if len_s1==len(list_2):
    len_count=int(len(set_1)/2)
    for _ in range(len_count):
        if set_1[count].issubset(set_1[count+1]):
            print(True)
        else:
            print(False)
    count+=1
else:
    print(False)


#1
'''s,n=set(input().split()),int(input())
print(all([s.issuperset(set(input().split())) for i in range(n)]))'''
#2
'''A = set(map(int, input().split()))
n = int(input())
counter = 0
for _ in range(n):
    N = set(map(int, input().split()))
    if A.issuperset(N) and len(A) > len(N):
        counter += 1
print(counter == n)'''
#3
'''7RiXxSec
3 days ago

a, z = set(map(int, input().split())), 0
r = int(input())
for _ in range(r):
    b = set(map(int, input().split()))
    if a.issuperset(b) and a != b:
        z += 1
if z == r:
    print("True")
else:
    print("False")

'''