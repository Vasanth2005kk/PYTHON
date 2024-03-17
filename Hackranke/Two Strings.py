num = int(input("enter the number:"))
for i in range(num):
    s1=input()
    s2=input()
    set_len=len((set(s1).intersection(set(s2))))
    if set_len==0:
        print("NO")
    else:
        print("YES")
