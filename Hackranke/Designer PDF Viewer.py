list_1=list(map(int,input().split(" ")))
word=input()
dic={
    "a":list_1[0],
    "b":list_1[1],
    "c":list_1[2],
    "d":list_1[3],
    "e":list_1[4],
    "f":list_1[5],
    "g":list_1[6],
    "h":list_1[7],
    "i":list_1[8],
    "j":list_1[9],
    "k":list_1[10],
    "l":list_1[11],
    "m":list_1[12],
    "n":list_1[13],
    "o":list_1[14],
    "p":list_1[15],
    "q":list_1[16],
    "r":list_1[17],
    "s":list_1[18],
    "t":list_1[19],
    "u":list_1[20],
    "v":list_1[21],
    "w":list_1[22],
    "x":list_1[23],
    "y":list_1[24],
    "z":list_1[25],
}
max_value=[]

for i in word:
    max_value.append(dic.get(i))

print(max(max_value)*len(word))