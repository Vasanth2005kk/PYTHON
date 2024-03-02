import itertools

string="abc"
output=[]
for i in range(1,len(string)+1):
    value=itertools.permutations(string,i)
    output.append(list(value))

for j in output:
    for k in j:
        print("".join(k))

