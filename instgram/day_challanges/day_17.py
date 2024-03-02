# remove extra spaces in the sentence
'''
rulese

1.no space at the beginning  and ending

2.only one space between words

'''

string=" programming     is  fin !!  ".strip(" ").split(" ")

ouput_string=""

for i in string:
    if i == "":
        continue
    else:
        ouput_string=ouput_string+" "+i

print(ouput_string.strip(" "))