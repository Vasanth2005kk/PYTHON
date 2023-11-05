'''
len()=>  The string count in the all letters in the case
type() => The returns the type of the object.
upper() => All the characters in a given string are uppers case.
lower() => All the characters in a given string are lower case.
capitalize() => The first character is the upper case
The title() => The first character in every word of the string is an upper case.
count() => Finds the number of times a specified value in the given string.
find() => Finds the first occurrence of the specified value. and find("a",5)=> iths 5 value in index 5 upper value.
replace() => Replaces a specified phrase with another specified phrase. pass in the 2 value in parametter
isalnum() => Checks whether all the characters in a given string is alphanumeric or not
isalpha() => returns True if all the characters in the string are alphabets
islower() => Checks if all characters in the string are lowercase
isupper() => Checks if all characters in the string are uppercase
strip() => The used to trim whitespaces from the string object
'''
# String And String Function

s="vasanth is programmer"
name="vasanth"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print("-______________________")
print(s.count("a"))
print(s.find("a",4))# start in the 0,1,2,3,4,5,6
                                #  v a s a n t h
print("-------------------------")
print(s.endswith("er"))
print(s.endswith("ers"))
print("--------------------------")
print(s.startswith("va"))
print(s.startswith("vasanth in"))
print("__________________")
print(len(s))               #not in strating in zero=(0)
print(len(name))            #starting in one=(1)
print("-------------------")
print(s.replace('vasanth',"@"))
print(s.replace('a', "@"))
print("____________________________")
a="jose123"
print(a.isupper())
print(a.islower())
print(a.isalnum())
print(a.isalpha())
print("___________________")
b="he\nis\ngood"
print(b.splitlines())
print(b.splitlines(True))
print("__________________________")
c= "python basic file,in,best,program"
print(c.split(","))
d= "python basic file in best program"
print(d.split(" "))
print("----------------------------")
space='     vasanth    '
print(len(space))
print(len(space.strip()))#all space remove
print(len(space.lstrip()))#space in remove leftside
print(len(space.rstrip()))#space in remove rightside
print("--------------------")
e="20.03.2005"
print(e.partition("0")) #starting in frist element in sembols