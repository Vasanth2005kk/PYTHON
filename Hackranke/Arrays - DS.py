n=int(input("entre the number:"))
list_1=input("enter :").split(" ")
if n==len(list_1):
    a=list_1[::-1]
    for i in a:
        print(i,end=" ")
