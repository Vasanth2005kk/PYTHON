import itertools

string=input().split(" ")

output=list(itertools.combinations_with_replacement(sorted(string[0]),int(string[1])))
for i in output:
    print("".join(i))
