
def factorial(n):
    count=1
    for i in range(1,n+1):
        count*=i
    return count

n=int(input())

print(factorial(n))