N=int(input())
data=[]
for i in range(N):
    data.append(list(input().split(" ")))

product_names=[]
for i in data:
    product_names.append(" ".join(i[:-1]))
dic={}
for name_num in data:
    dic[" ".join(name_num[:-1])]=name_num[-1]

for i,j in dic.items():
    print(i,product_names.count(i)*int(j))