from itertools import groupby

string=input()
output=[]
for i,j in groupby(string):
    output_1=(len((list(j))),int(i))
    output.append(output_1)
#print(output)
for j in output:
    print(j,end=" ")