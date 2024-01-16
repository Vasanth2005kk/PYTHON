n=int(input())
output=[]
for i in range(n):
    string_input=input()
    output.append(string_input[0::2]+" "+string_input[1::2])
for j in output:
    print(j)
