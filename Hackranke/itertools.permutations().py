value=list(input().split(" "))
#print(value)
str_1=value[0]
n=value[1]
from itertools import permutations
variable=list(permutations(str_1,int(n)))
#print(variable)
string=""
list_1=[]
for i in variable:
    for j in i:
        list_1.append(j)
#print(list_1)
for k in list_1:
    string+=k
#print(string)
from textwrap import wrap
split_words=(wrap(string,int(n)))
split_words.sort()
for i in split_words:
    print(i)