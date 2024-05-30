from collections import Counter

string=input()
dic=sorted(Counter(string).items(),key=lambda item:(-item[1],item[0]))

for i,j in dic[:3]:
    print(i,j)