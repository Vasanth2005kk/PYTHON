n = int(input())
s = set(map(int, input().split()))
range_1=int(input("enter the number:"))
for i in range(range_1):
    ste_words=input("discorde remove & pop name enter:").split(" ")
    if ste_words[0]=="discard":
        s.discard(int(ste_words[1]))
    elif ste_words[0]=="remove":
        s.remove(int(ste_words[1]))
    elif ste_words[0]=="pop":
        s.pop()
count=0
for i in s:
    count+=i
print(count)