list1=[]
temscore=[]
result=[]
for _ in range (int(input("Enter the range:"))):
    name = input("Enter the name:")
    score= float(input("Mark grade:"))
    list1.append([name, score])
    temscore.append(score)
temscore=list(set (temscore))
temscore.sort()
seclo=temscore[1]
for x in range(len(list1)):
    if list1[x][1]==seclo:
        result.append(list1[x][0])
result.sort()
for i in result:
    print(i)
