num=int(input())
ar=input().split()

add=0
if num == len(ar):
    for i in ar:
        add+=int(i)
    print(add)