num=int(input())
array=input().split()
count=0
if num==len(array):
    for i in array:
        count+=int(i)
    print(count)