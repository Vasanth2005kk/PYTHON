x,k=input().split(" ")
formula=input()
input_string=formula.replace("x",x)
if eval(input_string) == int(k):
    print(True)
else:
    print(False)