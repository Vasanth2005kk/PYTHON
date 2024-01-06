
import re

input_number=int(input())
arr=input().split()

#store
pastive=[]
negative=[]
zero=[]
if input_number==len(arr):
    for i in arr:
    #i=str(i)
        if i=="0":
            zero.append(i)
        elif re.findall("^-",i):
            negative.append(i)
        else:
            pastive.append(i)
dived_len=len(arr)
print("{0:.6f}".format(len(pastive)/dived_len))
print("{0:.6f}".format(len(negative)/dived_len))
print("{0:.6f}".format(len(zero)/dived_len))