arr=list(map(int,input().split(" ")))
list_1=[]
count=0
if arr[0]==arr[1]==arr[2]==arr[3]==arr[4]:
    count=arr[0]+arr[1]+arr[2]+arr[3]
    print(count,count)

else:
    for i in arr:
        for j in arr:
            if int(i)==int(j):
                continue
            else:
                count+=int(j)
        value=count
        count=0
        list_1.append(value)
    print(min(list_1),max(list_1))