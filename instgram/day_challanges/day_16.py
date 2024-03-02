#split the string 

string="  code id fun. !!!"

output=[]
for i in string.split(" "):
    if i != '':
        output.append(i)

print(output)