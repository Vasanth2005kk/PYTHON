'''set s_username="vasanth s_passwod="123456"
get input for uname and possword
create a function called validate.
if uname and password mactches the function should return true ,else false.'''

s_username="vasanth"
s_password="123456789"
name=input("username:")
password=input("password:")
def validate():
    if name==s_username:
        if password==s_password:
            return True
        else:
            return False
print(validate())


'''s_username="vasanth"
s_password="123456789"

def validate(name,password):
    if name==s_username:
        if password==s_password:
            return True
        else:
            return False
        
name=input("username:")
password=input("password:")
print(validate(name,password))'''

