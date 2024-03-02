for i  in range(1,101):
    if i==32 or i==77 or i==86:
        continue
    else:
        print(i)


#1
for i in range(1,101):
    if i not in [32,86,77]:
        print(i,end=" ")