N=int(input())
number=[]
for i in range(N):
    number.append(input())
for i in number:
    if i.startswith("9") and str(i).isdigit() and len(i) == 10: 
        print("YES")
    elif i.startswith("8")and str(i).isdigit() and len(i) == 10:
        print("YES")
    elif i.startswith("7")and str(i).isdigit() and len(i) == 10:
        print("YES")
    else:
        print("NO")