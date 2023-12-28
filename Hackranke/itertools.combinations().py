import  itertools
#string=["ABCD","3"]
string=input().split()
number=int(string[1])
output=[]
for i in range(2,number+1):
    split_tool = list(itertools.combinations(sorted(string[0]), i))
    for j in split_tool:
        output.append(sorted(j))
stord=[]
for k in output:
    stord.append("".join(k))
for f in sorted(string[0]):
    print(f)
for l in stord:
    print(l)

#1
'''from itertools import combinations
string, k = list(input().split())
for i in range(1, int(k)+1):
    for y in list(combinations(sorted(string), i)):
        print(''.join(y))'''
