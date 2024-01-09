row_subject=list(map(int,input().split(" ")))
#print(row_subject)

stord_list=[]
X=[]
count=0

for _ in range(row_subject[1]):
    mark=list(map(float,input().split(" ")))
    #print(mark)
    if len(mark)==row_subject[0]:
        stord_list.append(mark)
for k in stord_list:
    X+=[k]

for j in zip(*X):
     for i in j:
        count+=i
     print(count/row_subject[1])
     count=0
