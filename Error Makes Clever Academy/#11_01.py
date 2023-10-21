'''nested for loop
ex:1
output:
week:1
 day:1
 day:2
 day:3
week:2
 day:1
 day:2
 day:3
'''
for i in range(1,2+1):
    print("week:",i)
    for j in range(1,3+1):
        print("day:",j)
