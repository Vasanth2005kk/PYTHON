#multiline string in example program
para=[]
print("enter the para:")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
    #print(para)
    output=" ".join(para)
    print(output)