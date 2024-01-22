try:
    n = input()
    d = {}
    for i in range(int(n)):
        c = list(map(str,input().split(" ")))
        d.update({c[0]:c[1]})
        #c = input()
        #d[c[:-9]] = c[-8:]

    for i in range(int(n)):
        inp = str(input())
        key = inp
        value = d.get(inp, "Not found")
        if value != "Not found":
            print(f'{key}={value}')
        else:
            print(value)
except EOFError:
    pass 


'''try:
    n=int(input())

    phonebook={}

    for i in range(n):
        input_updates=list(map(str,input().split(" ")))
        phonebook.update({input_updates[0]:input_updates[1]})
        
    output=[]
    for j in range(n):
        input_values=input()
        if phonebook.get(input_values):
            output.append(f"{input_values}={phonebook.get(input_values)}")
        else:
            output.append("Not found")

    for k in output:
        print(k)
except EOFError as e:
    pass'''