import re

N = int(input("enter the number:"))
list_1=[]
for i in range(N):
    reg = input()
    try:
        re.compile(reg)
        list_1.append(True)
    except re.error:
        list_1.append(False)
for j in list_1:
    print(j)