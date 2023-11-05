'''write a program to read 10 number from the keybord and find their sum
and average.'''
list_1=[]
sum=0
for i in range(1,10+1):
    keybord=int(input("enter the number "+str(i)+" :"))
    list_1.append(keybord)
for j in list_1:
    sum+=j
print(sum)
print("average:",sum/10)
