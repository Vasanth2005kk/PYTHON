import re

email=input("enter the mail:")

email_1=re.split("@",email)

print(email_1)
if re.findall(".com$|.in$",email_1[1]):
    if re.findall("^[a-z]\D",email_1[0]):
        print("it's valid email")
    else:
        print("it's not valid email")
else:
    print("it's not valid email")