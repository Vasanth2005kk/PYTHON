import re
string=input()
list_1=[]
cap_letter=[]
for i in string:
    if re.findall("^[A-Z]",i):
        cap_letter.append(i)
        s=i.replace(i,",")
        list_1.append(s)
    else:
        list_1.append(i)
#print(list_1)
#print(cap_letter)
letter=""
for i in list_1:
    letter+=i
#print(letter)

split_letter=letter.split(",")
print(len(split_letter))