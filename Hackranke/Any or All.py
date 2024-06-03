N=int(input())
string_list=input().split()
if N == len(string_list):
    output=[]
    for i in string_list:
        if not (0<int(i)):
            output.clear()
        else:
            if i[::-1] == i:
                output.append(True)
            else:
                output.append(False)

    print(any(output))