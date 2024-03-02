import re

phragrph=input("enter the phragrph :")
words=re.split("\W",phragrph)

letter=0
word=0

repeterd_letter=[]

for i in words:
    if i :
        letter+=len(i)
        word+=1
        if words.count(i)>1:
            repeterd_letter.append(i)

print("<-------------------------->")
print("letter count :",letter)
print("words count :",word)

repeterd_letter_2=list(set(repeterd_letter))
for j in repeterd_letter_2:
    count_value=words.count(j)
    print(f"{j} : {count_value} times")