list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))

count_1=0
count_2=0
incrment=0
for _ in range(len(list_1)):
    if list_1[incrment]>list_2[incrment]:
        count_1+=1
    elif list_1[incrment]<list_2[incrment]:
        count_2+=1
    incrment+=1
print(count_1,count_2)
