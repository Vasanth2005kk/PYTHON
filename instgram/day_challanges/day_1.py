# palindrom or not

def plaindrome(string):
    if string == string[::-1]:
        return "you give a string is palindrom"
    else:
        return "you give a string is not palindrom"
    
s=input("Enter the string:")
output=plaindrome(s)
print(output)