# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0

#Im dealing with them as string not like INT
n,m = map(int, input().split())  #3 2
happiness_nos = input().split()
A = set(input().split())         #3 1
B = set(input().split())         #5 3

if n != len(happiness_nos) and m != len(A) and m != len(B) :
    print('Size Mismatch')

for i in happiness_nos:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)