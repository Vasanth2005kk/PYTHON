import re

string_input=input()

value=re.split("[cf]",string_input)

if re.findall("c$|C$",string_input):
    F=(9/5*int(value[0]))+32
    print(f"{F}F")
elif re.findall("f$|F$",string_input):
    C=(int(value[0])-32)*5/9
    print(f"{C}C")