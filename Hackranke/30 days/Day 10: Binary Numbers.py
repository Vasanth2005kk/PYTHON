
#print(len(max(list(map(str, bin(int(input().strip()))).lstrip("0b").split("0")))))

n=bin(int(input()))

output=n.lstrip("0b").split("0")
print(len(max(output)))