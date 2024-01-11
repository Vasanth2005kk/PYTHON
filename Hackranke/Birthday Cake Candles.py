num=int(input())
list_1=list(map(int,input().split(" ")))

list_1.sort()
x = list_1.count(list_1[-1])
print(x)

#1
'''count=0

for i in list_1:
    if i == max(list_1):
        count+=1
print(count)
'''
#2
'''x = list_1.count(max(list_1))
print(x)'''