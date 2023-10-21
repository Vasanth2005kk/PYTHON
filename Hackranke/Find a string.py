def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)#cdc ==>3
                          #7
    for s1 in range(0, len(string)):
        if string[s1:s1 + sub_len] == sub_string:
            counter += 1
    return print(counter)
string=input("enter the string:")#abcdcdc
sub_string=input("enter the string:")#cdc
count_substring(string,sub_string)
