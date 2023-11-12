A,B=input().split(" ")
a=int(A)
b=int(B)
c=".|."
for i in range(a//2):
    print((c*i).rjust(b//2-1,"-")+c+(c*i).ljust(b//2-1,"-"))
print("WELCOME".center(b,"-"))
for j in range(a//2,0,-1):
    print((c*(j-1)).rjust(b//2-1,"-")+c+(c*(j-1)).ljust(b//2-1,"-"))