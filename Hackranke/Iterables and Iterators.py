import itertools

num=int(input())
letter=input().split()
letter_index=int(input())

count=0
s=[]
for j in itertools.combinations(letter,letter_index):
    s.append(j)
for i in s:
    if letter[letter_index-1] in i:
        count+=1
count_2=len(s)
#print(count_2)
print("{0:.12f}".format(count/count_2))

'''import itertools

n = int(input())
l = input().split()
k = int(input())
ls = list(itertools.combinations(l, k))
count = 0
total = len(ls)
for pair in ls:
    if ("a" in pair):
        count+=1
print(count/total)
'''