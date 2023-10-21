string=input("enter the string:")
output=[[],[],[],[],[]]
for i in string:
    output[0].append(i.isalnum())
    output[1].append(i.isalpha())
    output[2].append(i.isdigit())
    output[3].append(i.isupper())
    output[4].append(i.islower())
for i in output:
    print(any(i))