def solution(inputString):
    print(sum([inputString.count(i)%2 for i in set(inputString)]) <= 1)

solution("abcad")

''''
string='abcad'
for i in set(string):
    print(string.count(i)%2)
    if string.count(i)%2:
        print(True)
    else:
        print(False)'''