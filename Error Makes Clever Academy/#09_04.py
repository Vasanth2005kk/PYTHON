'''count the number of even numbers between 1 to 10

sample output:
5
count the number of odd and even number between 1 to 10 and print it

sample output:
5
'''
count=0
o_count=0
for i in range(1,10+1):
    if i%2==0:
        count=count+1
    else:
        o_count=o_count+1
print(count)
print(o_count)
