n=int(input())
list_1=set(map(int,input().split(" ")))
costamer=int(input())
store=[]
for i in range(costamer):
    cst = tuple(map(int, input().split(" ")))
    store.append(cst)
N = list(set(store))  # [(4, 55), (5, 77)]
s = []
for i in list_1:
    for j in N:
        if j[0] == i:
            # print(j[0])
            s.append(j)
            # print(j)
se = set(s)
count = 0
for k in se:
    count += k[1]
print(count)

#1
'''n=int(input())
shoe_size=list(map(int,input().split()))
customers=int(input())
bill=0

for i in range(customers):
    size,price=list(map(int,input().split()))
    
    if size in shoe_size:
        bill+=price
        shoe_size.remove(size)
    
print(bill)'''
#2
'''from collections import defaultdict
number_of_shoes = int(input())
shoe_sizes = input()
shoe_sizes = shoe_sizes.split()
number_of_customers = int(input())
dict = defaultdict(list)
for i in range(number_of_customers):
    shoe_sizes_and_prizes = input()
    shoe_size, prize = shoe_sizes_and_prizes.split()
    dict[int(shoe_size)].append(prize)
new_shoe_sizes = []
for i in shoe_sizes:
    new_shoe_sizes.append(int(i))
amount = 0
for key, value in dict.items():
    count = 0
    length = len(value)
    for i in new_shoe_sizes:
        if key == i:
            count += 1
    if count == length:
        new_amount = sum([int(i) for i in value])
        amount += new_amount
    elif count == 0:
            continue
    else:
        for i, n  in enumerate(value):
            if i < count:
                amount += int(n)
            else:
                pass

print(amount)
'''