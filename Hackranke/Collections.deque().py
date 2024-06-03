from collections import deque

n=int(input())
D=deque()

for i in range(n):
    method=input().split(" ")
    if method[0] == "append" :
        D.append(int(method[1]))
    elif method[0] == "pop":
        D.pop()
    elif method[0] == "popleft":
        D.popleft()
    elif method[0] == "appendleft":
        D.appendleft(int(method[1]))

for i in D:
    print(i,end=" ")