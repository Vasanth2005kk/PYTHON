n,m=map(int,input().split())
A=[]
B=[]
for i in range(n):
    a=input()
    A.append(a)

for i in range(m):
    b=input()
    B.append(b)
   
 
for i in B:
    if i in A:
        for j in range(len(A)):
            if i==A[j]:
                print(j+1,end=" ")
        print()
    else:
        print(-1)


# n,m=map(int,input().split(" "))

# A=[]
# for i in range(n):
#     A.append(input())
# # print(A)

# B=[]
# for i in range(m):
#     B.append(input())
# # print(B)

# # A="".join(A)
# for i in B:
#     if i in A:
#         n=0
#         for j in range(A.count(i)):
#             indexing=1+(A.index(i,n))
#             n=indexing
#             print(indexing,end=" ")
#         print()
#     else:
#         print(-1)