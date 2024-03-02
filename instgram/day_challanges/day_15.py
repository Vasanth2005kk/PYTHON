# count vowels and consonants

string="coding".lower()

vowel=["a","e","i","o","u"]
vowel_count=0
consunt_count=0

for i in string:
    if i in vowel:
        vowel_count+=1
    elif i == ' ':
        continue
    else:
        consunt_count+=1

print("you give string in vowels is count :",vowel_count)
print()
print("you give string in consunt is count ",consunt_count)