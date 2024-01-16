def table(n,number=10):
    for i in range(1,number+1):
        print(f"{n} x {i} = {n*i}")

n=int(input())
table(n)