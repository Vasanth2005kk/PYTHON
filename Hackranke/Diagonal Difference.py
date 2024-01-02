from math import fabs

number=int(input())

list_1=[]
for i in range(number):
    input_values=list(map(int,input().split()))
    list_1.append(input_values)
#print(list_1)

#variable=[[-1,1,-7,-8],[-10,-8,-5,-2],[0,9,7,-1],[4,4,-2,1]]
num_1=0
num_2=0
incremet=0
decrimnt=number-1
for i in list_1:
    num_1+=i[incremet]
    incremet+=1
    num_2+=i[decrimnt]
    decrimnt-=1

#print(num_1)
#print(num_2)
total=num_1-num_2
print(int(fabs(total)))