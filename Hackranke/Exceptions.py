# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    try:
        a,b=map(int,input().split(" "))
        print(int(a/b))
    except ValueError as e:
        print("Error Code:",e)
    except ZeroDivisionError :
        print("Error Code: integer division or modulo by zero")
