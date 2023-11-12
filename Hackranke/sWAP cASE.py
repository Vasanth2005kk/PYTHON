def swap_case(s):
    string=[]
    for i in s:
        if i==i.lower():
            captal=i.upper()
            string.append(captal)
        elif i == i.upper():
            captal = i.lower()
            string.append(captal)
    #print(string)
    string_1=""
    for j in string:
        string_1+=j
    #print(string_1)
    return string_1
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)