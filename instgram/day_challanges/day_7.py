# factorial

num=0
count=1
if num != 0:
    for i in range(1,num+1):
        count*=i
    print(f"factorial of {num} is {count}")
else:
    print("0! is defined to be = 1")
