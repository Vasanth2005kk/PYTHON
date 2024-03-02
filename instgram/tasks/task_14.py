list_1=[]
print("only useing 4 commends:\n1.add\n2.print\n3.remove\n4.exit")
while True:
    key=input("enter your commend:")
    if "add" == key.lower():
        list_input=input().split()
        list_1.extend(list_input)
    elif "print" == key.lower():
        print(list_1)
    elif "remove"==key.lower():
        remove_string=input()
        list_1.remove(remove_string)    
    elif "exit" == key.lower():
        break
    else:
        break