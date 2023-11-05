'''count the number which are divisible by 3 and 5
range 1-100'''
count=0
for i in range(1,100+1):
    if i%3==0 and i%5==0:
       # print(i)
        count=count+1
print(count)
