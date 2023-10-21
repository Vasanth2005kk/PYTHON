lists=[]
print("1.insert\n2.print\n3.remove\n4.append\n5.sort\n6.pop\n7.reverse")
number=int(input("enter the number:"))
for i in range(number):
    N=input("enter your keys:").split()
    #print(N)
    if N[0]=="insert":
        i,e=map(int,N[1:])
        lists.insert(i,e)
    elif N[0]=="print":
        print(lists)
    elif N[0]=="remove":
        e=int(N[1])
        lists.remove(e)
    elif N[0]=="append":
        e=int(N[1])
        lists.append(e)
    elif N[0]=="sort":
        lists.sort()
    elif N[0]=="pop":
        lists.pop()
    elif N[0]=="reverse":
        lists.reverse()
    '''else:
        print("not this keyyy!")
        break
    '''