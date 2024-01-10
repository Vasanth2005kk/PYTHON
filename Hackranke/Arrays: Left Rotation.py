inputlen_rotation=list(map(int,input().split(" ")))
list_input=list(map(int,input().split(" ")))

if inputlen_rotation[0]==len(list_input):
    list_input.extend(list_input[0:inputlen_rotation[1]])
    for i in list_input[0:inputlen_rotation[1]]:
        list_input.remove(i)
    #print(list_input)
    for i in list_input:
        print(i,end=" ")