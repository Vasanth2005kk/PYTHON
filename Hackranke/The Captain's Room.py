import collections

va = int(input())
l = list(map(int, input().split(" ")))
s = collections.Counter(l)
# print(s)
for i, j in s.items():
    if j == 1:
        print(i)

#1
'''
import collections
va=int(input())
l=list(map(int,input().split(" ")))
s=collections.Counter(l)
#print(s)
#print(s.keys())
s1=list(s.keys())
print(s1[-1])
'''