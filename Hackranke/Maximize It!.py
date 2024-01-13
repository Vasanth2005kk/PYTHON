from itertools import product
k, mod = map(int, input().split())
cur, ans = 0, 0
combos, lst = [], []
for _ in range(k):
    line = list(map(int, input().split()))
    lst.append(line[1:])
    
for item in list(product(*lst)):
    cur = 0
    for ele in item:
        cur += ele**2
    ans = max(ans, cur % mod)
print(ans)

#1
'''
from itertools import product

row_mod=list(map(int,input().split(" ")))

list_strode=[]
output=[]
count=0


for i in range(row_mod[0]):
    input_list=list(map(int,input().split(" ")))
    list_strode.append(input_list)

for j in product(*list_strode):
    for k in j:
        count+=k*k
    output.append(count)
    count=0

print(max(output)%row_mod[1])  
'''