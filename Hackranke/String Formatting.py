def print_formatted(n):
    list_2=[]
    for i in range(1,n+1):
        #print(i,end=" ")
        octal=oct(i)
        octal_1=octal.removeprefix("0o")
        #print(octal.removeprefix("0o"),end=" ")
        hexdecimal=hex(i)
        hexdecimal_1=hexdecimal.removeprefix("0x")
        #print(hexdecimal.removeprefix("0x"),end=" ")
        binary=bin(i)
        binary_1=binary.removeprefix("0b")
        #print(binary.removeprefix("0b"))
        list_1=[i,octal_1,hexdecimal_1,binary_1]
        list_2.append(list_1)
    #print()
    for j in list_2:
        for k in j:
            print(k,end=" ")
        print()

print_formatted(17)
#1
'''def print_formatted(number):
    for i in range(1,  number+ 1):
        w = len("{0:b}".format(number))
       # print("w:",w)
        dec = i
        oc = oct(i)[2:]
        h = str(hex(i).upper()[2:]).rjust(w)
        b = str(bin(i)[2:]).rjust(w)

        print("{:{width}} {:{width}o} {:{width}s} {:{width}s}".format(dec, i, h, b, width=w))
if __name__ == '__main__':
   # n = int(input())
    print_formatted(17)'''
